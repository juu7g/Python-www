# Python-www
Web���색�C�u����

## �T�v Description
Web���색�C�u����

## ���e Contents

- WebSite�N���X `en` ScrolledFrame class
	- get_html()���\�b�h `en` wrapped_grid() class method
	- get_text_from_html()���\�b�h
	- output_to_file()���\�b�h

## WebSite�N���X

### ���\�b�h Method
- `get_html(self, url:str)`  
	- ����
		- `url`�Furl
	- �߂�l
		- str�Fhtml
		- str�F�G���[���e(�G���[���Ȃ����͋󕶎�)
	- ����
		- �w�肵��url��html�������擾���܂�  
		- �G���[���������ꍇ�A�G���[���e��Ԃ��܂�

- `get_text_from_html(self, html:str, tag:str="div", cls:str="hatenablog-entry")`  
	- ����
		- `html`�Fhtml�������w��
		- `tag`�F�e�L�X�g���擾����Ώۂ̃^�O(����ȉ��̕������擾�Ώ�)
		- `cls`�F�e�L�X�g���擾����Ώۂ̃N���X
	- �߂�l
		- str�F�e�L�X�g
	- ����
		- �w�肵��html��������e�L�X�g���擾���܂�
		- cls�N���X������tag�^�O�̎q���̃e�L�X�g���擾���܂�

- `output_to_file(self, text:str, ext:str="txt")`  
	- ����
		- `text`�F�e�L�X�g
		- `ext`�F�t�@�C���g���q
	- ����
		- text���t�@�C���ɏo�͂��܂�
		- �t�@�C�����͌Z���tests�f�B���N�g���Ɂuhtml_yymmddHHMM.txt�v

## �ˑ��֌W Requirement

- Python 3.8.5  
- requests 2.31.0
- beautifulsoup4 4.12.2

## �v���O�����̐����T�C�g

- [gTTS��mpg123�ō��e�L�X�g�ǂݏグ�A�v���yPython�z - �v���O�����ł��������ł��邩��](https://juu7g.hatenablog.com/entry/Python/text-to-speech/speech-text)  


## ��� Authors
juu7g

## ���C�Z���X License
���̃\�t�g�E�F�A�́AMIT���C�Z���X�̂��ƂŌ��J����Ă��܂��BLICENSE.txt���m�F���Ă��������B 