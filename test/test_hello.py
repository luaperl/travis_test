import sys

sys.path.insert(0, './')
import ngh_func.hello as h

def test_hello_en():
	assert h.hello_en() == 'Hello'

def test_hello_ko():
	assert h.hello_ko() == '안녕'

def test_hello_repeat():
	assert h.hello_repeat('en', 2) == 'Hello_Hello'
	assert h.hello_repeat('en', 1) == 'Hello'
	assert h.hello_repeat('ko', 3) == '안녕_안녕_안녕'