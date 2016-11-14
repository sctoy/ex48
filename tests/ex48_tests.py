from nose.tools import *
import lexicon

def test_directions():
	assert_equal(lexicon.scan("North"),[('direction', 'north')])
	result = lexicon.scan("north south east")
	assert_equal(result, [('direction', 'north'),
						  ('direction', 'south'),
						  ('direction', 'east')])
						  
def test_verbs():
	assert_equal(lexicon.scan("go"),[('verbs', 'go')])
	result = lexicon.scan("go kill eat")
	assert_equal(result, [('verbs', 'go'),
						  ('verbs', 'kill'),
						  ('verbs', 'eat')])
						  
def test_stops():
	assert_equal(lexicon.scan("the"), [('stop', 'the')])
	result = lexicon.scan("the in of")
	assert_equal(result, [('stop', 'the'),
						  ('stop', 'in'),
						  ('stop', 'of')])
						  
def test_nouns():
	assert_equals(lexicon.scan("door"), [('nouns', 'door')])
	result = lexicon.scan("door bear princess")
	assert_equals(result, [('nouns', 'door'),
						   ('nouns', 'bear'),
						   ('nouns', 'princess')])
						   
def test_numbers():
	assert_equals(lexicon.scan("1234"), [('number', 1234)])
	result = lexicon.scan("1234 4321 8765")
	assert_equals(result, [('number', 1234),
						   ('number', 4321),
						   ('number', 8765)])
						   
def test_errors():
	assert_equals(lexicon.scan("qwerty"), [('error', 'qwerty')])
	result = lexicon.scan("qwerty ytrewq asdfg")
	assert_equals(result, [('error', 'qwerty'),
							('error', 'ytrewq'),
							('error', 'asdfg')])