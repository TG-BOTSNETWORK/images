�
    �O�g��  �                   �  � S SK JrJr  S SKJrJr  S SKJrJrJ	r	J
r
JrJrJr  S SKJr  S SKJr  S SKJr  \" SSS	S
S9r\" S5      r\S   r\S   r\S   r\S   rSrS rS rS rS rS rS r\R?                  \R@                  " S5      5      S\4S j5       r!\RE                  5       S\S\4S j5       r#\R?                  \R@                  " S5      \RH                  -  5      S\4S j5       r%\R?                  \R@                  " S 5      \RH                  -  5      S\4S! j5       r&\RO                  5       S" 5       r(\RS                  5         \*" S#5        g$)%�    )�Client�filters)�	ParseMode�ChatMemberStatus)�InlineQueryResultArticle�InputTextMessageContent�InlineKeyboardMarkup�InlineKeyboardButton�Message�ChatMemberUpdatedr   )�MongoClient)�datetime)�RPCError�pytgcalls_boti;?U� 5c096f7e8fd4c38c035d53dc5a85d768z.7923309063:AAEk3A4VfzZLKs7FI_c99hYXBfhnFVke0Zc)�api_id�api_hash�	bot_tokenzmmongodb+srv://VEEZWORKS:SANTHU7981@veezworks.stpqs.mongodb.net/?retryWrites=true&w=majority&appName=veezworks�pytgcalls_db�users�searches�groupsl   |Z�q c                 �j   � U UU[         R                  " 5       S.n[        R                  SU 0SU0SS9  g )N)�user_id�username�
first_name�	joined_atr   �$setT��upsert)r   �now�users_collection�
update_one)r   r   r   �users       �pytg_assistant.py�add_userr&   .   s;   � ��� ��\�\�^�	�D� ����G� 4�v�t�n�T��R�    c                 �2   � [         R                  SU 05        g )Nr   )r"   �
delete_one)r   s    r%   �del_userr*   7   s   � �����G� 4�5r'   c                  �*   � [         R                  5       $ �N)�searches_collection�find� r'   r%   �get_searchesr0   :   s   � ��#�#�%�%r'   c                 �h   � U U[         R                  " 5       S.n[        R                  SU 0SU0SS9  g )N)�group_id�
group_name�
created_atr2   r   Tr   )r   r!   �groups_collectionr#   )r2   r3   �groups      r%   �	add_groupr7   =   s9   � �� ��l�l�n��E�
 � � �*�h�!7�&�%��QU� �Vr'   c                  �*   � [         R                  5       $ r,   )r5   r.   r/   r'   r%   �
get_groupsr9   E   s   � ��!�!�#�#r'   c                 �   � [         R                  5       R                  U 5      nSnU H"  n[         R                  SUS   05        US-  nM$     U$ )Nr   �_id�   )r-   r.   �limitr)   )�count�searches_to_delete�searches_deleted�searchs       r%   �reset_searchesrB   H   sV   � �,�1�1�3�9�9�%�@����$���&�&��v�e�}�'=�>��A��� %� �r'   �start�messagec              �   �  #   � UR                   R                  nUR                   R                  nUR                   R                  n[	        X#U5        SU S3nUS-  nUR                  U[        R                  S9I S h  v�N   g  N7f)Nz
**Welcome u
   !** 🎉

z�I'm your PyTgCalls Documentation Bot. search something in inline search `@PyTgCallsDocsBot search` to get started with the PyTgCalls library!

��
parse_mode)�	from_user�idr   r   r&   �replyr   �MARKDOWN)�clientrD   r   r   r   �welcome_texts         r%   rC   rC   P   s}   � � ����"�"�G�� � �)�)�H��"�"�-�-�J��W�
�+��
�|�<�8�L��  h�  h�L�
�-�-���1C�1C�-�
D�D�D�s   �A;B�=B�>BrL   �updatec              �   �`  #   � UR                   (       a,  UR                  (       a  UR                  R                  (       d  g U R                  5       I S h  v�N nUR                  nUR                  R                  R                  U:X  a�  UR                  R
                  [        R                  [        R                  4;   ag  UR                   R                  nUR                   R                  n[        XE5        Sn[        [        SSS9//5      nU R                  XFUS9I S h  v�N   g g g  N� N	7f)Nu�   ✅ **Thanks for adding me to the group!** 🎉

📌 You can now search for anything related to PyTgCalls directly here.
🔍 Click the **Search Here** button below to start your search!u   🔍 Search Here� �� switch_inline_query_current_chat)�reply_markup)�chat�new_chat_memberr$   �get_merI   �statusr   �MEMBER�ADMINISTRATOR�titler7   r	   r
   �send_message)rL   rN   �bot_info�bot_idr2   r3   �cap_text�keyboards           r%   �new_member_addedr`   \   s�   � � ��;�;�f�4�4�F�<R�<R�<W�<W���]�]�_�$�H��[�[�F� 	���#�#�&�&�&�0����%�%�*:�*A�*A�CS�Ca�Ca�)b�b��;�;�>�>���[�[�&�&�
��(�'�P� 	�
 (�!�"4�WY�Z�[�)
� �� �!�!�(�8�!�L�L�L� 	c� 	1�	 %�$ 	M�s%   �AD.�D*�CD.�"D,�#D.�,D.�statsc              �   �x  #   � UR                  S5      I S h  v�N nUR                  S5      I S h  v�N   UR                  5       I S h  v�N   [        R	                  0 5      n[
        R	                  0 5      nSnUSU S3-  nUSU S3-  nUR                  U[        R                  S9I S h  v�N   g  N� N� Nm N7f)NzGetting stats.....zUploading stats.....z**Bot Stats**:

zTotal Users: �
zTotal Searches: rF   )�
reply_text�	edit_text�deleter"   �count_documentsr-   r   rK   )rL   rD   �msg�total_users�total_searches�
stats_texts         r%   ra   ra   t   s�   � � � �"�"�#7�8�
8�C�
�-�-�.�
/�/�/�
�.�.�
���"�2�2�2�6�K�(�8�8��<�N�%�J��M�+��b�1�1�J��$�^�$4�B�7�7�J�
�-�-�
�y�/A�/A�-�
B�B�B� 9�/�� C�sD   �B:�B2�B:�B4�B:�B6�	A#B:�,B8�-B:�4B:�6B:�8B:�resetc              �   �v  #   � UR                   R                  [        :w  a  g  [        UR                  R                  5       S   5      n[        U5      nUR                  SU S35      I S h  v�N   [        X5      I S h  v�N   g ! [        [        4 a    UR                  S5      I S h  v�N     g f = f NH N77f)Nr<   z'Usage: /reset <count> (e.g., /reset 45)zSuccessfully deleted z
 searches.)rH   rI   �OWNER_ID�int�text�split�
IndexError�
ValueErrorrJ   rB   ra   )rL   rD   r>   r@   s       r%   rl   rl   �   s�   � � ������x�'����G�L�L�&�&�(��+�,�� &�e�,��
�-�-�/�0@�/A��L�
M�M�M�
��
 � � �� �
�#� ��m�m�E�F�F�F���� N� �sR   � B9�&B �	#B9�,B5�-B9�?B7� B9�$B2�)B,�*B2�/B9�1B2�2B9�7B9c              �   �(  #   � UR                   R                  5       R                  5       n/ nU(       a+  [        R	                  U[
        R                  " 5       S.5        U(       aD  UR                  [        SU S3[        SU S35      SU S3S[        [        S	S
S9//5      S95        UR                  S5      (       aG  UR                  [        S[        S[        R                  S9SS[        [        S	S
S9//5      S95        GO�UR                  S5      (       aG  UR                  [        S[        S[        R                  S9SS[        [        S	SS9//5      S95        GORUR                  S5      (       aG  UR                  [        S[        S[        R                  S9SS[        [        S	SS9//5      S95        GO�UR                  S5      (       a:  UR                  [        S[        S5      S S[        [        S	S!S9//5      S95        GO�UR                  S"5      (       a:  UR                  [        S#[        S$5      S%S[        [        S	S&S9//5      S95        GOUUR                  S'5      (       aG  UR                  [        S([        S)[        R                  S9S*S[        [        S	S+S9//5      S95        GO�UR                  S,5      (       aG  UR                  [        S-[        S.[        R                  S9S/S[        [        S	S0S9//5      S95        GO�UR                  S15      (       aG  UR                  [        S2[        S3[        R                  S9S4S[        [        S	S5S9//5      S95        GO>UR                  S65      (       aG  UR                  [        S7[        S8[        R                  S9S9S[        [        S	S:S9//5      S95        GO�UR                  S;5      (       aG  UR                  [        S<[        S=[        R                  S9S>S[        [        S	S?S9//5      S95        GO�UR                  S@5      (       a:  UR                  [        SA[        SB5      SCS[        [        SDSES9//5      S95        GO4UR                  SF5      (       a:  UR                  [        SG[        SH5      SIS[        [        SDSJS9//5      S95        GO�UR                  SK5      (       aG  UR                  [        SL[        SM[        R                  S9SNS[        [        SDSOS9//5      S95        GO�UR                  SP5      (       aG  UR                  [        SQ[        SR[        R                  S9SSS[        [        SDSTS9//5      S95        GO*UR                  SU5      (       aG  UR                  [        SV[        SW[        R                  S9SXS[        [        SDSYS9//5      S95        GO�UR                  SZ5      (       aG  UR                  [        S[[        S\[        R                  S9S]S[        [        SDS^S9//5      S95        GOpUR                  S_5      (       aG  UR                  [        S`[        Sa[        R                  S9SbS[        [        SDScS9//5      S95        GOUR                  Sd5      (       aG  UR                  [        Se[        Sf[        R                  S9SgS[        [        SDShS9//5      S95        GO�UR                  Si5      (       aG  UR                  [        Sj[        Sk[        R                  S9SlS[        [        SDSmS9//5      S95        GOYUR                  Sn5      (       aF  UR                  [        So[        Sp[        R                  S9SqS[        [        SDSrS9//5      S95        O�UR                  Ss5      (       aF  UR                  [        St[        Su[        R                  S9SvS[        [        SDSwS9//5      S95        O�UR                  Sx5      (       aF  UR                  [        Sy[        Sz[        R                  S9S{S[        [        S|S}S9//5      S95        OEUR                  [        S~[        S[        R                  S9S�S[        [        S�S�S�9//5      S95        UR                  US�S�9I S h  v�N    UR                  U5      I S h  v�N   g  N N! [          a  n[#        S�U 35         S nAg S nAff = f7f)�N)�query�	timestampu   🔍 Search Results for '�'z**Results for 'ac  ':**

Here are some inline search suggestions based on your query:

1. **Quick Start Guide**: Guide for getting started with PyTgCalls.
2. **Installation Guide**: Install PyTgCalls on your system.
3. **About**: Learn about the PyTgCalls project.
4. **Change Logs**: View the latest updates to PyTgCalls.

You can refine your search by typing more details!zShowing results related to 'z'.zNhttps://raw.githubusercontent.com/TG-BOTSNETWORK/images/main/images/search.pngu   📖 Read Full Documentationz&https://pytgcalls.github.io/PyTgCalls/)�url)rZ   �input_message_content�description�	thumb_urlrS   )�a�aboutu   📚 About PyTgCallsa  **About PyTgCalls**

This project allows making Telegram calls using MtProto and WebRTC, thanks to the power of the NTgCalls library and @evgeny-nadymov.

**Features**:
- Prebuilt wheels for macOS, Linux, and Windows.
- Supports all types of MTProto libraries: Pyrogram, Telethon, and Hydrogram.
- Works with voice chats in channels and chats.
- Join as channels or chats.
- Mute/unmute, pause/resume, stop/play, volume control, and more.

Explore the full potential of PyTgCalls and enhance your Telegram experience!rF   z,Learn more about PyTgCalls and its features.zLhttps://raw.githubusercontent.com/TG-BOTSNETWORK/images/main/images/logo.png)�i�install�gu   ⚙️ PyTgCalls Install Guidea�  **Install PyTgCalls**

1. **Install Python 3.8+**: Ensure Python 3.8 or higher is installed on your system.

2. **Install PyTgCalls**: Use pip to install the latest stable version:

   ```bash
   pip3 install -U py-tgcalls
   ```

3. **Install Development Version**: To try the latest features, install directly from the GitHub master branch:

   ```bash
   pip3 install -U git+https://github.com/pytgcalls/pytgcalls
   ```

4. **Verify Installation**: Open a Python shell and import PyTgCalls to verify the installation:

   ```python
   import pytgcalls
   print(pytgcalls.__version__)
   ```

   You should see the version number printed.z$Detailed steps to install PyTgCalls.zChttps://pytgcalls.github.io/PyTgCalls/Install%20Guide#Install=GuiderC   u   🚀 Quick Start Guidea=  **Quick Start with PyTgCalls**

1. **Install PyTgCalls**: `pip3 install -U py-tgcalls`

2. **Choose Your MTProto Client**: PyrogramMod (ex Pyrogram), Telethon, or Hydrogram.

3. **Get Your Telegram API Key**: Obtain it from [my.telegram.org](https://my.telegram.org).

4. **Set Up Your Script**: Replace `client` and `chat_id` values with your own.

5. **Save and Run**: Save the file as `main.py` and execute it to start streaming audio.

6. **Join the Community**: Engage with other developers and users.

7. **Enjoy the API**: Explore the full capabilities of PyTgCalls.z-Detailed steps to get started with PyTgCalls.z?https://pytgcalls.github.io/PyTgCalls/Quick%20Start#Quick=Start�	c_methodsu   🔧 Calling MethodsaX  Here it is calling methods.

[Basic Usage](https://pytgcalls.github.io/PyTgCalls/Calling%20Methods#Basic=Usage)
[Basic step-by-step](https://pytgcalls.github.io/PyTgCalls/Calling%20Methods#Basic=step-by-step)
[Asynchronous Calls](https://pytgcalls.github.io/PyTgCalls/Calling%20Methods#Asynchronous=Calls)
[Asynchronous step-by-step](https://pytgcalls.github.io/PyTgCalls/Calling%20Methods#Asynchronous=step-by-step)

`At this point, we have successfully installed PyTgCalls and installed an MTProto client; we are now aiming towards the core of the library. It's time to start playing with the API!`z3Explore Calling Methods in PyTgCalls with examples.z7https://pytgcalls.github.io/PyTgCalls/Calling%20Methods)�h�up�ur|   u   ⚙️ Handling Updatedu�  `🔹 Calling API methods sequentially is cool, but what if, for example, the list of participants changes? This page covers updates and how to handle such events in PyTgCalls. Let's have a look at how they work.`

[Registering a Handler](https://pytgcalls.github.io/PyTgCalls/Handling%20Updates#Registering=a=Handler)
[Defining Updates](https://pytgcalls.github.io/PyTgCalls/Handling%20Updates#Registering=a=Handler)
[Using Decorators](https://pytgcalls.github.io/PyTgCalls/Handling%20Updates#Using=Decorators)z4Explore Handling Updates in PyTgCalls with examples.z8https://pytgcalls.github.io/PyTgCalls/Handling%20Updates�ffmpeg_parameters�additional_ffmpeg_parametersa�  **Append parameters to ffmpeg**

**Example:**
```python
from pyrogram import Client
from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioQuality, MediaStream, VideoQuality

app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)

call_py = PyTgCalls(app)
call_py.start()

remote = 'http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4'
call_py.play(
    -1001234567890,
    MediaStream(
        remote,
        AudioQuality.HIGH,
        VideoQuality.HD_720p,

        # You can add --video or --audio to the ffmpeg
        # command line to specify to what you want to add these parameters
        ffmpeg_parameters='EVERYTHING BEFORE THE INPUT (-i) '
                          '-atmid '
                          'EVERYTHING AFTER THE INPUT (-i) '
                          '-atend '
                          'EVERYTHING AFTER ALL ARGUMENTS',
    ),
)
idle()
```zAAppend custom ffmpeg parameters for media streaming in PyTgCalls.zwhttps://github.com/pytgcalls/pytgcalls/blob/master/example/additional_ffmpeg_parameters/additional_ffmpeg_parameters.py�capture�c_mica�  **Capture Microphone Audio**

**Example:**
```python
from pyrogram import Client
from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls.media_devices import MediaDevices
from pytgcalls.types import MediaStream

app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)

call_py = PyTgCalls(app)
call_py.start()

call_py.play(
    -1001234567890,
    MediaStream(
        MediaDevices.get_audio_devices()[0],
    ),
)
idle()
```z1Capture and stream microphone audio in PyTgCalls.zUhttps://github.com/pytgcalls/pytgcalls/blob/master/example/capture_mic/example_mic.py�c_apiz
Custom APIa�  **Use Custom API with PyTgCalls**

**Example:**
```python
import json
import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import CustomApi, idle

app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)

ca = CustomApi()

# Handle Custom API Requests
@ca.on_update_custom_api()
async def custom_api_request(request: dict):
    print(request)
    return {'response': 'BYE'}

@app.on_message(filters.regex('!test'))
def test_handler(client: Client, message: Message):
    print(
        requests.post(
            'http://localhost:24859/',
            json.dumps({'answer': 'HI'}),
        ).json()
    )

app.start()
ca.start()
idle()
```z?Use a custom API server to bind PHP or other APIs to PyTgCalls.zThttps://github.com/pytgcalls/pytgcalls/blob/master/example/custom_api/example_api.py�fifozFIFO Conversionai  **Play Stream from FIFO with PyTgCalls**

**Example:**
```python
import asyncio
import atexit
import os
import signal
import time

from ntgcalls import InputMode
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message

from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls.types.raw import AudioStream
from pytgcalls.types.raw import Stream

app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)

call_py = PyTgCalls(app)
proc = {}

@app.on_message(filters.regex('!test'))
async def test_handler(client: Client, message: Message):
    global proc
    file = 'input.webm'
    output_file = 'input_fifo.raw'
    os.mkfifo(output_file)
    proc[message.chat.id] = await asyncio.create_subprocess_shell(
        cmd=(
            'ffmpeg '
            '-y -i '
            f'{file} '
            '-f s16le '
            '-ac 1 '
            '-ar 48000 '
            '-acodec pcm_s16le '
            f'{output_file}'
        ),
        stdin=asyncio.subprocess.PIPE,
    )

    while not os.path.exists(output_file):
        time.sleep(0.125)
    await call_py.play(
        message.chat.id,
        Stream(
            AudioStream(
                input_mode=InputMode.File,
                path=output_file,
            ),
        ),
    )

def close_all_process():
    global proc
    for i in proc:
        try:
            proc[i].send_signal(signal.SIGINT)
            proc[i].wait(timeout=3)
        except subprocess.TimeoutExpired:
            proc[i].kill()

# AVOID ZOMBIE FFMPEG PROCESS
atexit.register(close_all_process)
call_py.start()
idle()
```z3Play a stream from FIFO using PyTgCalls and FFmpeg.zZhttps://github.com/pytgcalls/pytgcalls/blob/master/example/fifo_conversion/example_fifo.py�	p2p_callszP2P Examplea  **Play Stream from Private Call using PyTgCalls**

**Example:**
```python
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message

from pytgcalls import filters as fl
from pytgcalls import PyTgCalls
from pytgcalls.types import ChatUpdate
from pytgcalls.types import MediaStream
from pytgcalls.types import Update

app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)
call_py = PyTgCalls(app)

test_stream = 'http://docs.evostream.com/sample_content/assets/' \
              'sintel1m720p.mp4'

@app.on_message(filters.regex('!call'))
async def play_handler(_: Client, message: Message):
    await call_py.play(
        message.chat.id,
        MediaStream(
            test_stream,
        ),
    )

@app.on_message(filters.regex('!hangup'))
async def stop_handler(_: Client, message: Message):
    await call_py.leave_call(
        message.chat.id,
    )

@call_py.on_update(fl.chat_update(ChatUpdate.Status.INCOMING_CALL))
async def incoming_handler(_: PyTgCalls, update: Update):
    await call_py.mtproto_client.send_message(
        update.chat_id,
        'You are calling me!',
    )
    await call_py.play(
        update.chat_id,
        MediaStream(
            test_stream,
        ),
    )
call_py.run()
```z2Play a stream from a private call using PyTgCalls.zUhttps://github.com/pytgcalls/pytgcalls/tree/master/example/p2p_example/example_p2p.py�piped_audio_callszPiped Audio Callsa�  **Play Audio Using FFmpeg for Live Conversion**

**Example Code:**
```python
from pyrogram import Client
from pytgcalls import idle, PyTgCalls
from pytgcalls.types import MediaStream

app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)

call_py = PyTgCalls(app)
call_py.start()

audio_file = 'input.webm'

call_py.play(
    -1001234567890,
    MediaStream(
        audio_file,
        video_flags=MediaStream.Flags.IGNORE,
    ),
)

idle()
```
z=Stream audio using FFmpeg for live conversion with PyTgCalls.u   📖 View Full Examplezchttps://github.com/pytgcalls/pytgcalls/blob/master/example/piped_audio_calls/example_piped_audio.py�piped_image_callsu   🖼️ Piped Image Callsu  📚 **Play Audio and Image Using FFmpeg for Live Conversion**

**Example Code:**
```python
from pyrogram import Client
from pytgcalls import idle, PyTgCalls
from pytgcalls.types import MediaStream, VideoQuality

app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)

call_py = PyTgCalls(app)
call_py.start()

audio_file = 'input.webm'
call_py.play(
    -1001234567890,
    MediaStream(
        'test.png',
        audio_path=audio_file,
        video_parameters=VideoQuality.HD_720p,
    ),
)
idle()
```
zGStream audio and image using FFmpeg for live conversion with PyTgCalls.zchttps://github.com/pytgcalls/pytgcalls/blob/master/example/piped_image_calls/example_piped_image.py�raw_streamingu   📼 Raw Streamingu�  🎬 **Play PCM16L and RAW_VIDEO from Disk**

**Example Code:**
```python
import os
import time

from ntgcalls import InputMode
from pyrogram import Client
from pytgcalls import idle, PyTgCalls
from pytgcalls.types.raw import (
    AudioParameters, AudioStream,
    VideoParameters, VideoStream, Stream
)

app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)

call_py = PyTgCalls(app)
call_py.start()

audio_file = 'audio.raw'
video_file = 'video.raw'

while not os.path.exists(audio_file) or not os.path.exists(video_file):
    time.sleep(0.125)

call_py.play(
    -1001234567890,
    Stream(
        AudioStream(
            InputMode.File,
            audio_file,
            AudioParameters(bitrate=48000),
        ),
        VideoStream(
            InputMode.File,
            video_file,
            VideoParameters(width=640, height=360, frame_rate=24),
        ),
    ),
)
idle()
```z@Stream raw PCM16L audio and raw video from disk using PyTgCalls.zYhttps://github.com/pytgcalls/pytgcalls/blob/master/example/raw_streaming/example_video.py�remote_piped_playu   🌍 Remote Piped Playu5  🎥 **Play a Stream from a Remote Link with FFmpeg**

**Example Code:**
```python
from pyrogram import Client
from pytgcalls import idle, PyTgCalls
from pytgcalls.types import MediaStream, AudioQuality, VideoQuality

app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)

call_py = PyTgCalls(app)
call_py.start()

remote = 'http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4'

call_py.play(
    -1001234567890,
    MediaStream(
        remote,
        AudioQuality.HIGH,
        VideoQuality.HD_720p,
    ),
)
idle()
```zBStream a remote audio/video link using FFmpeg for live conversion.zdhttps://github.com/pytgcalls/pytgcalls/blob/master/example/remote_piped_play/example_remote_piped.py�remote_stream_with_headeru   🌐 Remote Stream with Headeru�  📡 **Play a Remote Stream with Custom Headers**

**Example Code:**
```python
from pyrogram import Client
from pytgcalls import idle, PyTgCalls
from pytgcalls.types import MediaStream, AudioQuality, VideoQuality, Browsers

app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)

call_py = PyTgCalls(app)
call_py.start()

remote = 'http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4'

call_py.play(
    -1001234567890,
    MediaStream(
        remote,
        AudioQuality.HIGH,
        VideoQuality.HD_720p,
        headers={
            'User-Agent': Browsers().chrome_windows,
        },
    ),
)
idle()
```z6Stream a remote link using FFmpeg with custom headers.zqhttps://github.com/pytgcalls/pytgcalls/blob/master/example/remote_stream_with_header/remote_stream_with_header.py�screen_sharingu%   🖥️ Screen Sharing with PyTgCallsu�  📡 **Share Your Screen in Telegram Calls**

**Example Code:**
```python
from pyrogram import Client
from pytgcalls import idle, PyTgCalls
from pytgcalls.media_devices import MediaDevices
from pytgcalls.types import MediaStream

app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)

call_py = PyTgCalls(app)
call_py.start()

call_py.play(
    -1001234567890,
    MediaStream(
        MediaDevices.get_screen_devices()[0],
    ),
)
idle()
```z6Stream your screen in a Telegram call using PyTgCalls.z\https://github.com/pytgcalls/pytgcalls/blob/master/example/screen_sharing/example_desktop.py�screen_sharing_micu*   🖥️🎤 Screen Sharing with Microphoneu!  📡 **Share Your Screen with Microphone in Telegram Calls**

**Example Code:**
```python
from pyrogram import Client
from pytgcalls import idle, PyTgCalls
from pytgcalls.media_devices import MediaDevices
from pytgcalls.types import MediaStream

app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)

call_py = PyTgCalls(app)
call_py.start()

call_py.play(
    -1001234567890,
    MediaStream(
        MediaDevices.get_screen_devices()[0],
        audio_path=MediaDevices.get_audio_devices()[0],
    ),
)
idle()
```zLStream your screen with microphone audio in a Telegram call using PyTgCalls.zdhttps://github.com/pytgcalls/pytgcalls/blob/master/example/screen_sharing_mic/example_desktop_mic.py�simple_callsu1   🎵 Simple Example: High-Level PyTgCalls Methodsuv
  📡 **Simple Example Using High-Level Methods in PyTgCalls**

**Example Code:**
```python
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message

from pytgcalls import filters as fl
from pytgcalls import idle, PyTgCalls
from pytgcalls.types import ChatUpdate
from pytgcalls.types import GroupCallParticipant
from pytgcalls.types import MediaStream
from pytgcalls.types import Update

app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)

call_py = PyTgCalls(app)
test_stream = 'http://docs.evostream.com/sample_content/assets/' \
              'sintel1m720p.mp4'

@app.on_message(filters.regex('!play'))
async def play_handler(_: Client, message: Message):
    await call_py.play(
        message.chat.id,
        MediaStream(
            test_stream,
        ),
    )

@app.on_message(filters.regex('!cache'))
async def cache_handler(_: Client, _m: Message):
    print(call_py.cache_peer)

@app.on_message(filters.regex('!ping'))
async def ping_handler(_: Client, _m: Message):
    print(call_py.ping)

@app.on_message(filters.regex('!pause'))
async def pause_handler(_: Client, message: Message):
    await call_py.pause_stream(
        message.chat.id,
    )

@app.on_message(filters.regex('!resume'))
async def resume_handler(_: Client, message: Message):
    await call_py.resume_stream(
        message.chat.id,
    )

@app.on_message(filters.regex('!stop'))
async def stop_handler(_: Client, message: Message):
    await call_py.leave_call(
        message.chat.id,
    )

@app.on_message(filters.regex('!change_volume'))
async def change_volume_handler(_: Client, message: Message):
    await call_py.change_volume_call(
        message.chat.id,
        50,
    )

@app.on_message(filters.regex('!status'))
async def get_play_status(client: Client, message: Message):
    await client.send_message(
        message.chat.id,
        f'Current seconds {await call_py.played_time(message.chat.id)}',
    )

@call_py.on_update(
    fl.chat_update(
        ChatUpdate.Status.KICKED | ChatUpdate.Status.LEFT_GROUP,
    ),
)
async def kicked_handler(_: PyTgCalls, update: Update):
    print(f'Kicked from {update.chat_id} or left')

@call_py.on_update(fl.stream_end)
async def stream_end_handler(_: PyTgCalls, update: Update):
    print(f'Stream ended in {update.chat_id}', update)

@call_py.on_update(
    fl.call_participant(GroupCallParticipant.Action.JOINED),
)
async def participant_handler(_: PyTgCalls, update: Update):
    print(f'Participant joined in {update.chat_id}', update)

@call_py.on_update()
async def all_updates(_: PyTgCalls, update: Update):
    print(update)

call_py.start()
idle()
```zRLearn to use high-level methods like play, pause, resume, and more with PyTgCalls.zYhttps://github.com/pytgcalls/pytgcalls/blob/master/example/simple_calls/example_simple.py�telethon_exampleu$   🎥 PyTgCalls with Telethon Exampleu  📡 **Using PyTgCalls with Telethon**

**Example Code:**
```python
from telethon import TelegramClient

from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream

app = TelegramClient(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)

call_py = PyTgCalls(app)
call_py.start()
test_stream = 'http://docs.evostream.com/sample_content/assets/' \
              'sintel1m720p.mp4'

call_py.play(
    -1001234567890,
    MediaStream(
        test_stream,
    ),
)

idle()
```z=Learn how to use PyTgCalls with Telethon for media streaming.z_https://github.com/pytgcalls/pytgcalls/blob/master/example/telethon_example/example_telethon.py�video_callsu&   🎬 Play Video with PyTgCalls Exampleu�  📡 **Play Audio & Video with FFmpeg Conversion**

**Example Code:**
```python
from pyrogram import Client

from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream

app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)

call_py = PyTgCalls(app)
call_py.start()
video_file = 'test.mkv'

call_py.play(
    -1001234567890,
    MediaStream(
        video_file,
    ),
)

idle()
```z@Learn how to stream audio and video using PyTgCalls with FFmpeg.z]https://github.com/pytgcalls/pytgcalls/blob/master/example/video_calls/example_piped_video.py�
youtube_dlu.   🎥 Play YouTube Video with PyTgCalls Exampleu�  📹 **Play YouTube Video using YoutubeDL with PyTgCalls**

**Example Code:**
```python
from pyrogram import Client

from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioQuality
from pytgcalls.types import MediaStream
from pytgcalls.types import VideoQuality

app = Client(
    'py-tgcalls',
    api_id=123456789,
    api_hash='abcdef12345',
)

call_py = PyTgCalls(app)
call_py.start()

call_py.play(
    -1001234567890,
    MediaStream(
        'https://www.youtube.com/watch?v=msiLgFkXvD8',
        AudioQuality.HIGH,
        VideoQuality.HD_720p,
        ytdlp_parameters='--proxy URL',
    ),
)

idle()
```zFStream YouTube videos in your group call with PyTgCalls and YoutubeDL.z[https://github.com/pytgcalls/pytgcalls/blob/master/example/youtube_dl/youtube_dl_example.py�examples_queryu   📚 PyTgCalls Example QueriesaP  Here are some examples for **PyTgCalls**:

- additional_ffmpeg_parameters
- capture_mic
- custom_api
- fifo_conversion
- p2p_example
- piped_audio_calls
- piped_image_calls
- raw_streaming
- remote_piped_play
- remote_stream_with_header
- screen_sharing
- screen_sharing_mic
- simple_calls
- telethon_example
- video_calls
- youtube_dl
z&List of example queries for PyTgCalls.u   📖 See More Examplesz:https://github.com/pytgcalls/pytgcalls/tree/master/exampleu   📖 PyTgCalls Documentationum  **Welcome to PyTgCalls!** 🎙️

PyTgCalls is a powerful library for handling Telegram voice and video calls using Python. Below are key sections to help you explore its features:

**Getting Started** 🚀

- Calling Methods
- Handling Updates
- Examples
**API Reference**
- Client
- Custom API
- Media Devices
- Decorators
- Filters
- Using Filters
- Using Handlers
**Available Enums**
- AudioQuality
- Call Status
- Call Type
- ChatUpdate Status
- GroupCallParticipant Action
- MediaStream Flags
- VideoQuality

Type a keyword to explore more details about any of these sections! for more you can try document websitez3Comprehensive guide to PyTgCalls features and APIs.u   🔍 Search AgainrP   rQ   r<   )�results�
cache_timezAn RPC error occurred: )ru   �strip�lowerr-   �
insert_oner   r!   �appendr   r   r	   r
   �
startswithr   rK   �answerr   �print)rL   �inline_queryru   r�   �es        r%   r�   r�   �   s%  � � ����$�$�&�,�,�.�E��G���&�&��X�\�\�^�'T�U�����$�1�%���:�&=�%�e�W� -I� I�'� ;�5�'��D�j�1�-�.L�Rz�{�|����	
�* ����'�'����$�,�&=�d�  )�1�1�'� K�h�1�-�.L�Rz�{�|���!�	
�2 
�	�	�/�	0�	0����$�6�&=�D�   )�1�1�#'�& C�h�1�-�.L�  SX�  Y�  Z���/�	
�@ 
�	�	�'�	"�	"����$�.�&=�X�  )�1�1�
'� L�h�1�-�.L�  ST�  U�  V����	
�. 
�	�	�+�	&�	&��^�^� �(�"9�  ;\
� #�M�d�-�)�*H�  OH�  I�  J���	
�� 
�	�	�/�	0�	0��^�^� �+�"9�  ;@	� #� O�d�-�)�*H�  OI�  J�  K���	
�� 
�	�	�-�	.�	.��^�^� �0�"9��@ %�-�-�C"#�F \�d�-�)�*H�  OH�  I�  J���O,	
�.�^ 
�	�	�)�	$�	$��^�^� ��"9��. %�-�-�1#�4 L�d�-�)�*H�  Of�  g�  h���=#	
�%�L 
�	�	�'�	"�	"��^�^� ��"9��> %�-�-�A!#�D Z�d�-�)�*H�  Oe�  f�  g���M+	
�-�\ 
�	�	�&�	!�	!��^�^� �#�"9�A�D %�-�-�GD#�J N�d�-�)�*H�  Ok�  l�  m���SN	
�P�b 
�	�	�+�	&�	&��^�^� ��"9�-�\ %�-�-�_0#�b M�d�-�)�*H�  Of�  g�  h���k:	
�<�z 
�	�	�-�	.�	.��^�^� �%�"9��#�2 X�d�-�)�*B�  In�  o�  p���;"	
�$�J 
�	�	�-�	.�	.��^�^� �-�"9��#�4 b�d�-�)�*B�  In�  o�  p���=#	
�%�L 
�	�	�/�	*�	*��^�^� �&�"9�'�P %�-�-�S*#�V [�d�-�)�*B�  Id�  e�  f���_4	
�6�n 
�	�	�-�	.�	.��^�^� �*�"9��0 %�-�-�3#�6 ]�d�-�)�*B�  Io�  p�  q���?$	
�&�N 
�	�	�5�	6�	6��^�^� �2�"9��6 %�-�-�9#�< Q�d�-�)�*B�  I|�  }�  ~���E'	
�)�T 
�	�	�*�	+�	+��^�^� �9�"9��, %�-�-�/#�2 Q�d�-�)�*B�  Ig�  h�  i���;"	
�$�J 
�	�	�.�	/�	/��^�^� �>�"9��. %�-�-�1#�4 g�d�-�)�*B�  Io�  p�  q���=#	
�%�L 
�	�	�.�	)�	)��^�^� �E�"9�Q�d %�-�-�gT#�j m�d�-�)�*B�  Id�  e�  f���s^	
�`�B 
�	�	�,�	-�	-��^�^� �8�"9��0 %�-�-�3#�6 X�d�-�)�*B�  Ij�  k�  l���?$	
�&�N 
�	�	�-�	(�	(��^�^� �:�"9��. %�-�-�1#�4 [�d�-�)�*B�  Ih�  i�  j���=#	
�%�L 
�	�	�,�	'�	'��^�^� �B�"9��6 %�-�-�9#�< a�d�-�)�*B�  If�  g�  h���E'	
�)�T 
�	�	�*�	+�	+��^�^� �2�"9�!�" %�-�-�%#�( A�d�-�)�*B�  IE�  F�  G���1	
��F 	���$�4�&=�@�4  )�1�1�7'�: R�h�1�-�.A�df�g�h���C&�(	
�T �
�
�g�!�
�
<�<�<�-��!�!�'�*�*�*� =�*��� -��'��s�+�,�,��-�sN   �cd�	c)�
d�c- �#c+�$c- �(d�+c- �-
d�7d
�d�
d�dzBOT STARTED
DEVELOPER: SANTHUN)+�pyrogramr   r   �pyrogram.enumsr   r   �pyrogram.typesr   r   r	   r
   r   r   �pymongor   r   �pyrogram.errorsr   �apprL   �dbr"   r-   r5   rn   r&   r*   r0   r7   r9   rB   �
on_message�commandrC   �on_chat_member_updatedr`   �privatera   rl   �on_inline_queryr�   �runr�   r/   r'   r%   �<module>r�      s�  ��* &� 7�� � �  � � $��_�X�8Z�  gW�  X��	�  E�  
F���N����g�;� ���n� ��x�L� ���S�6�&�W�$�� �������(�)�	E�� 	E� *�	E� ����M�6� M�3D� M� �M�. �������(�7�?�?�:�;�
C�� 
C� <�
C� �������(�7�?�?�:�;�
!�� 
!� <�
!� ����x-� �x-�v ���	� �&� 'r'   