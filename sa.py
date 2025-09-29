import json

def extract_strictly_descending_diffs(paths_dict, category_diff_threshold=0.2, api_diff_threshold=0.2):
    # ===== スコアファイル読み込み =====
    all_scores = {}
    for label, path in paths_dict.items():
        with open(path, "r", encoding="utf-8") as f:
            all_scores[label] = json.load(f)

    # ===== 共通の mashup のみ対象 =====
    mashup_names = set.intersection(*(set(scores.keys()) for scores in all_scores.values()))

    # ===== 結果格納用 =====
    selected = {}

    for mashup in mashup_names:
        cat_f1s = {label: all_scores[label][mashup]["category_f1"] for label in paths_dict}
        api_f1s = {label: all_scores[label][mashup]["api_final_f1"] for label in paths_dict}

        # 🔴 整数の 0 が含まれる場合は除外（0.0 はOK）
        all_f1s = list(cat_f1s.values()) + list(api_f1s.values())
        if any(type(x) is int and x == 0 for x in all_f1s):
            continue

        # 比較順は固定（辞書順ではなく意図通りに）
        labels = ["top6", "top3_low3", "low6"]
        cat_values = [cat_f1s[label] for label in labels]
        api_values = [api_f1s[label] for label in labels]

        # 📉 単調減少 & スコア差チェック
        is_strict_descending = (
            cat_values[0] > cat_values[1] > cat_values[2] and
            api_values[0] > api_values[1] > api_values[2]
        )
        satisfies_diff = (
            (cat_values[0] - cat_values[2]) >= category_diff_threshold and
            (api_values[0] - api_values[2]) >= api_diff_threshold
        )

        if is_strict_descending and satisfies_diff:
            selected[mashup] = {
                "category_f1s": {label: round(cat_f1s[label], 3) for label in labels},
                "category_diff": round(cat_values[0] - cat_values[2], 3),
                "api_final_f1s": {label: round(api_f1s[label], 3) for label in labels},
                "api_diff": round(api_values[0] - api_values[2], 3)
            }

    # ===== JSON 保存 =====
    output_path = "diff_f1_strict_descending_filtered.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(selected, f, indent=2, ensure_ascii=False)

    print(f"✅ 順序・差分を満たす mashup 数: {len(selected)} 件")
    print(f"→ {output_path} に保存しました")


# ===== 実行 =====
if __name__ == "__main__":
    paths = {
        "top6": "./output/gpt/bert_top6/f1_instance_scores.json",
        "top3_low3": "./output/gpt/bert_top3_low3/f1_instance_scores.json",
        "low6": "./output/gpt/bert_low6/f1_instance_scores.json"
    }

    # カテゴリ・APIの差分しきい値を個別指定
    extract_strictly_descending_diffs(
        paths_dict=paths,
        category_diff_threshold=0.2,
        api_diff_threshold=0.2
    )