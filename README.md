# :twisted_rightwards_arrows:CycleSquareGAN

<p align="center"><img src="https://github.com/user-attachments/assets/77b9b31e-37e0-4b98-b06e-2a60e5237ea1"></p>
<p align="center"><img src="https://github.com/user-attachments/assets/b31ea122-c09b-4c3d-97b2-843d1e71ad33"></p>

## 목차
1. [프로젝트 개요](#프로젝트-개요)
2. [연구의 필요성](#연구의-필요성)
3. [프로젝트 소개](#프로젝트-소개)
4. [논문](#논문)


## 프로젝트 개요
**이 프로젝트는 [CycleGAN GitHub](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)에서 파생된 코드입니다.**

- **기간**: 2023.01-2023.06
- **팀원 & 역할 분담**:
  - 김진기(kjg6462@naver.com): 데이터 셋 취득 및 평가
  - 이동현(tjsqlfkdls@naver.com): 딥러닝 모델을 SLAM에 결합, ROS
  - [장우현](https://github.com/dngus1683): 딥러닝 모델 구상
  - [허정범](https://github.com/okpocandy): 딥러닝 모델 구상
- **사용 언어**: python
- **사용 툴**: 
    - Visual Studio Code
    - jupyter
    - tensorflow == 2.10.0
    - cudatoolkit == 11.7.0
    - cuDnn == 8.4
- **실습 환경**: Ubuntu 20.04

## 연구의 필요성
- 모바일 로봇이 다양한 서비스 분야에서 활용되면서 비전 센서를 이용한 로봇의 정밀한 위치 추정이 널리 연구되고 있지만 실외 환경에서 모바일 로봇의 위치 추정 정확도는 조도의 변화에 영향을 받게 된다. 
- 이를 극복하기 위해 pix2pix, CycleGAN등의 딥러닝 모델을 이용하여 이미지를 변환할 수 있다.
- 하지만 기존 모델은 특정 두 도메인만의 변환에만 집중되어 있다.
- 즉, 다양한 시간 대의 이미지들을 하나의 이미지로 변환하기 위해서는 각각에 맞는 딥러닝 모델이 필요하다는 문제점이 있다.


## 프로젝트 소개
- [CycleGAN 모델](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)을 기반으로 다양한 시간대의 이미지를 일정한 시간대의 이미지로 변환하는 방법을 제안한다. 
- 기존 CycleGAN의 Generator 구조를 수정하여 도메인 변환을 통해 시간에 의존적인 이미지를 독립적으로 개선하는 것이 목표다.
- 제안한 방법은 Generator 사이에 중간 단계인 Middle Bridge Space라는 구조를 도입하는 것이다.
- 모든 시간 대의 이미지를 Middle Bridge Space 이미지로 변환 후, 이를 SLAM에 유리한 이미지로 변환한다.
- 또한, SSIM-loss를 활용하여 이미지 데이터 처리에 유용하도록 Loss 계산을 개선한다.




## 논문
![Image](https://github.com/user-attachments/assets/06aeceae-e48e-4257-82eb-92dcab4a0c7d)

![Image](https://github.com/user-attachments/assets/e4be310a-16f1-4761-8c70-6641ce8fdb49)
