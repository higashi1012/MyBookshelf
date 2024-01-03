"""
第1章 ネットワーク基礎知識

OSI参照モデル
アプリケーション層
プレゼンテーション層
セッション層
トランスポート層
ネットワーク層
データリンク層
物理層

OSI参照モデルでは、各層で何をするかという「役割」を定義している。
各層の「役割」を定義しているのが「プロトコル」
「プロトコル」とは約束ごと、その中身は「仕様」
そのプロトコルの仕様に準拠した製品・通信手段を私達は利用している。

ざっくりイメージ（メール送信の場合）
アプリケーション層→本文と送り先など情報を分割。HTTP
プレゼンテーション→情報をコンピュータが分かる形式に変換。HTML
セッション層→情報の伝達方法を定義。1通ごと送る、5通まとめて送るなど
トランスポート層→コネクションの確立・切断。データが到達したかの確認
ネットワーク層→ここでアドレス情報などが付けられてデータリンク層に送られる
データリンク層→機器同士のデータのやり取り
物理層→データの0や1を電圧としてやり取り


第2章 TCP/IP 基礎知識
TCP/IPといえばインターネットのプロトコル

TCP/IPモデル
アプリケーション層
トランスポート層
インターネット層
ネットワークインターフェース層
（ハードウェア）

◯インターネット層
IP(Internet Protocol)→パケットを配送し、インターネット全体にパケットを送り届けるためのプロトコル
ICMP(Internet Control Message Protocol)→パケットの送信元に以上を知らせるために使われるプロトコル
ARP(Address Resolution Protocol)→送り先のアドレスをIPアドレスから取得するプロトコル

◯トランスポート層
TCP(Transmission Control Protocol)
UDP(User Datagram Protocol)
"""