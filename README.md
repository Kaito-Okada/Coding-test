# Coding-test

コーディングテスト用です．

# Features

- `fixpoint-1.py`  
   監視ログファイルを読み込み、各サーバアドレスにおいて，故障か否かを表示します．故障の場合は，故障の期間についても表示します．

- `fixpoint-2.py`  
   上記機能を修正，N 回以上連続してタイムアウトした場合のみ故障とみなします．

- `fixpoint-3.py`  
   上記の機能に加え，直近 m 回の平均応答時間が t ミリ秒を超えた場合は，サーバが過負荷状態になっているとみなし，過負荷状態の期間を表示します．

- `fixpoint-4.py`

# Requirement

- Python 3.7.6

# Usage

- `fixpoint-1.py`

```bash
python fixpoint-1.py filename
```

- `fixpoint-2.py`

```bash
python fixpoint-2.py filename n
```

n(int):タイムアウトの許容回数[回]

- `fixpoint-3.py`

```bash
python fixpoint-3.py filename n m t
```

n(int):タイムアウトの許容回数[回]
m(int):平均値を出力するための直近範囲
t(int or float):許容応答時間[ミリ秒]

- `fixpoint-4.py`

```bash
python fixpoint-4.py filename n m t
```

# Note

## 対応しているログファイルについて

- 最大容量は 1 日分のログファイルを想定
- 1 日分のログファイルのログ収集間隔、最大 1 秒毎を想定
- 確認結果は以下に示すカンマ区切りの形式のみ対応  
  ＜確認日時＞,＜サーバアドレス＞,＜応答結果＞ - 確認日時：YYYYMMDDhhmmss の形式。ただし、年＝ YYYY（4 桁の数字）、月＝ MM（2 桁の数字。以下同様）、日＝ DD、時＝ hh、分＝ mm、秒＝ ss - サーバアドレスは、ネットワークプレフィックス長付きの IPv4 アドレスである。 - 応答結果には、ping の応答時間がミリ秒単位で記載される。ただし、タイムアウトした場合は"-"(ハイフン記号)となる。

# Author

作成情報を列挙する

- 名前：岡田 魁人(Okada Kaito)
- 所属：岡山大学大学院自然科学研究科電子情報システム工学専攻自然言語処理研究室所属
- E-mail：pdrj11bt@s.okayama-u.ac.jp
