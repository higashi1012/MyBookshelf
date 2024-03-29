"""
☆マルチタスク
コンピュータやデバイスが異なるアプリケーション（この場合、メールシステムとゲームシステム）を同時に実行していること。
マルチタスクでは、オペレーティングシステム（OS）が複数のアプリケーション間でCPU時間を分割し、各アプリケーションが一度に少し実行されるようにしている。
これにより、ユーザーは両方のアプリケーションが同時に動作しているかのように感じることができる。
実際には、OSが非常に高速にタスク間で切り替えを行っているだけ。

☆マルチスレッド
ブラウザでウェブページを表示する際の動きは、典型的なマルチスレッドの例。
ウェブブラウザは複数のスレッドを使用して、異なるタスクを同時に実行する。

☆マルチプロセス
ウェブブラウザのタブ
各タブを異なるプロセスとしているため、1つのタブでエラーが起きても
別のタブに影響しない

例えば、ブラウザで複数タブを開く場合、マルチプロセス構造と考えることが出来る。
各プロセス内部でマルチスレッドが細かなタスク管理を行っている。
"""