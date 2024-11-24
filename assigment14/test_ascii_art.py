import pytest
from main_copy import generate_ascii_art, load_art_style  

def test_generate_ascii_art():
    
    standard_expected = '''\
    _   _
    | \\ | |
    |  \\| |
    | . ` |
    | |\\  |
    |_| \\_|
    '''

    shadow_expected = '''\
    _|      _|
    _|_|    _|
    _|  _|  _|
    _|    _|_|
    _|      _|
    '''

    thinkertoy_expected = '''\
    o   o
    |\\  |
    | \\ |
    |  \\|
    o   o
    '''


   
    standard_art = load_art_style(r"C:\Users\Жангелди\Desktop\Nfactorial\ascii-art-project-1-doctorrin-main\standard.txt")
    shadow_art = load_art_style(r"C:\Users\Жангелди\Desktop\Nfactorial\ascii-art-project-1-doctorrin-main\shadow.txt")
    thinkertoy_art = load_art_style(r"C:\Users\Жангелди\Desktop\Nfactorial\ascii-art-project-1-doctorrin-main\thinkertoy.txt")

   
    result = generate_ascii_art("N", standard_art)
    print(result)  
    assert result == standard_expected.strip(), f"Expected: {standard_expected}, but got: {result}"

    
    result = generate_ascii_art("N", shadow_art)
    print(result)  
    assert result == shadow_expected.strip(), f"Expected: {shadow_expected}, but got: {result}"

    
    result = generate_ascii_art("N", thinkertoy_art)
    print(result)  
    assert result == thinkertoy_expected.strip(), f"Expected: {thinkertoy_expected}, but got: {result}"

