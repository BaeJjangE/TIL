# 가상머신(Oracle VM VirtualBox) & CentOS 7

- Virtualbox 링크
  https://www.virtualbox.org/wiki/Downloads
- Putty(Linux 가독성을 위한 도구 사용)
  https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html
    - 64-bit x86:   putty.exe	<-- 다운로드
    - putty 설정 방법
      1. putty 실행
      2. 왼쪽 항목에서 [Window] 하단에 [Appearance] 클릭
      3. 글자 설정(글꼴, 글자 크기)
      4. 왼쪽 항목에서 [Session] 선택
      5. Host Name 부분에 ip 주소를 입력(192.168.56.10)
      6. Saved Sessions 부분에 ip 주소를 입력(192.168.56.10)
      7. save 버튼 클릭
      8. [open] 버튼 클릭
      9. [accept] 버튼 클릭
      10. 사용자 입력란에 root 입력
      11. 비밀번호 입력
    
- Virtualbox 설치
  1. VirtualBox-6.1.32-149290-Win.exe 실행
  2. [Next] 버튼 클릭
  3. Custom setup 단계에서 [Next] 클릭
  4. [Next] 클릭
  5. [Next] 클릭
  6. [Yes] 클릭
  7. Ready to Install 단계에서 [Install] 클릭

- Virtualbox 네트워크 설정
  Nat-Network

  1. [파일] 버튼 클릭 후 [환경 설정] 클릭
  2. [네트워크] 항목 클릭
  3. 우측 상단 [플러스] 버튼을 클릭하여 NatNetwork 추가
  5. 생성된 NatNetwork 더블 클릭
  4. DHCP 지원 체크 박스를 해제
  5. [확인] 버튼 클릭

- Host-only

  1. [파일] 버튼 클릭 후 [호스트 네트워크 관리자] 클릭
  2. 네트워크가 없는 경우 [만들기] 클릭
  3. [VirtualBox Host-Only Ethernet Adapter] 더블 클릭 후 네트워크 확인
  - IPv4 주소 : 192.168.56.1
  - IPv4 서브넷 마스크 : 255.255.255.0
  4. 우측 상단에 DHCP 서버 사용함 체크를 해제

- 가상머신 만들기

  1. virtualbox 메인화면에서 [도구] 항목에서 [새로 만들기] 클릭
  2. 이름 : Centos7#1
  - 종류 : Linux
  - 버전 : Red Hat (64-bit)
  3. [다음] 버튼 클릭
  4. 메모리 크기 : 1024 MB
  5. [다음] 버튼 클릭
  6. [지금 새 가상 하드 디스크 만들기] 선택
  7. [만들기] 클릭
  8. VDI 선택 후 [다음] 클릭
  9. [동적 할당] 선택 후 [다음] 클릭
  10. 8.00 GB 확인 후 [만들기] 클릭

- 가상머신 네트워크 설정

  1. 만든 Centos7#1 가상머신 선택 후 [설정] 클릭
  2. [네트워크] 항목 클릭
  3. 어뎁터 1 설정
  - 네트워크 어댑터 사용하기 체크
  - 다음에 연결됨 : NAT 네트워크
  - 이름 : NatNetwork
  4. 어뎁터 2 설정
  - 네트워크 어댑터 사용하기 체크
  - 다음에 연결됨 : 호스트 전용 어댑터
  - 이름 : VirtualBox Host-Only Ethernet Adapter
  5. [확인] 버튼 클릭

- Centos 이미지 삽입

  1. [저장소] 항목 클릭
  2. 컨트롤러 : IDE 우측에 "CD +" 모양 클릭
  3. [추가] 버튼 클릭
  4. centos7 파일을 찾아서 [열기] 버튼 클릭
  5. [선택] 클릭
  6. [확인] 버튼 클릭

- iso 파일을 8버전에서 7버전으로 바꾼 후에 진행

  1. 저장소에서 [추가] - centos 7 선택
  2. centos8 우클릭으로 연결 해제하기

- 8버전에서 7버전 바꾼 후 실행이 안 될 경우 가상 머신을 삭제

  - [모든 파일 지우기] 후 가상 머신 재설치

- Centos 설치

  1. 가상 머신 선택 후 [시작] 버튼 클릭
  2. [Install CentOS 7] 엔터
  3. [한국어] 지정 후 [계속 진행] 클릭
  4. [설치 대상] 항목 진입(enter)
  5. [완료] 클릭
  6. [설치 시작] 클릭
  7. [ROOT 암호] 클릭
  8. 비밀번호 설정
  9. [완료] 클릭

- 마우스 잡힘 해결 방법

  1. virtualbox 메인 화면에서 [파일] 클릭
  2. [환경 설정] 클릭
  3. [입력] 클릭
  4. [가상 머신(M)] 클릭
  5. 호스트 키 조합 부분의 단축키 설정
  - Ctrl + Alt
  6. [확인]

- 창 크기 키우기(가상머신 내에서 설정)
  [머신] - [설정] - [디스플레이] - [크기 조정 비율]

  - 크기 조정 비율을 증가 설정

- centos 로그인
  localhost login: root	<-- 입력
  Password: 		<-- 입력
  [root@localhost ~] #	<-- 로그인 완료