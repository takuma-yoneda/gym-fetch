# FROM nvidia/cuda:11.3.1-runtime-ubuntu18.04
FROM nvidia/cuda:10.2-runtime-ubuntu18.04
ENV LANG=C.UTF-8

RUN apt-get update && apt-get install -y git vim tree curl unzip xvfb patchelf \
    ffmpeg cmake swig wget libglu1-mesa-dev libgl1-mesa-dev libosmesa6-dev \
    cmake libopenmpi-dev python3-dev zlib1g-dev
RUN apt-get update && apt-get install -y libssl-dev libcurl4-openssl-dev  # Needed for pyCurl
RUN apt-get update && apt-get install -y qtbase5-dev qtdeclarative5-dev libglib2.0-0

# Download mujoco
RUN mkdir /root/.mujoco && \
    cd /root/.mujoco  && \
    curl -O https://www.roboti.us/download/mujoco200_linux.zip  && \
    unzip mujoco200_linux.zip && \
    mv /root/.mujoco/mujoco200_linux /root/.mujoco/mujoco200

RUN wget https://roboti.us/file/mjkey.txt -P /root/.mujoco/

ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/root/.mujoco/mujoco200/bin
ENV MUJOCO_PY_MJPRO_PATH /root/.mujoco/mujoco200
ENV MJLIB_PATH /root/.mujoco/mujoco200/bin/libmujoco200.so
ENV MJKEY_PATH /root/.mujoco/mjkey.txt

RUN apt-get install -y libssl-dev libcurl4-openssl-dev
RUN apt-get install -y python3.8-dev python3-pip
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN ln -s /usr/bin/python3.8 /usr/bin/python
RUN python -m pip install --upgrade pip

ENV PIP_NO_CACHE_DIR=off

RUN pip install pytest pytest-forked lz4 pyyaml qt5-py
# RUN pip install --pre torch torchvision torchaudio -f https://download.pytorch.org/whl/nightly/cu113/torch_nightly.html
RUN pip install torch
RUN pip install kornia opencv-python
# RUN pip install tensorflow tensorboard
# RUN git clone https://github.com/openai/baselines.git
# RUN cd baselines && pip install -e .
RUN pip install glfw numpy Cython imageio cffi lockfile

#RUN apt-get install software-properties-common
RUN apt-get install -y libgl1-mesa-glx libosmesa6
RUN apt-get install -y libglew-dev
# RUN pip install git+git://github.com/deepmind/dm_control.git
# RUN pip install gym-dmc
# used for egl rendering
# ENV MUJOCO_GL egl
#ENV LD_PRELOAD /usr/lib/x86_64-linux-gnu/libGLEW.so
#:/usr/lib/x86_64-linux-gnu/libGL.so.1

# Lacking dependencies
RUN pip install pandas scikit-image  # ml-logger dependency

RUN pip install cffi Cython
RUN pip install mujoco-py==2.0.2.5

# RUN pip install 'git+http://github.com/geyang/gym-distracting-control.git@ae4ab85599e084849397f6c7731c632f1c130e12#egg=distracting_control'
RUN pip install -I gym==0.19.0
RUN pip install xmltodict  # Nick Hansen's generalization-benchmark env dependency

# Download DAVIS dataset required for distracting-control
# ADD https://data.vision.ee.ethz.ch/csergi/share/davis/DAVIS-2017-trainval-480p.zip /tmp/
# RUN unzip /tmp/DAVIS-2017-trainval-480p.zip -d /root/dataset && rm /tmp/DAVIS-2017-trainval-480p.zip
# ENV DC_BG_PATH /root/dataset/DAVIS/JPEGImages/480p

RUN pip install jaynes ml_logger waterbear params-proto functional-notations
RUN pip install gym-fetch
