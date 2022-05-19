#This program manipulate comp202coin by encrypt and decrypt it
#Ziwei Hu 260889365
import coin_utils
from coins import *
import random
import doctest


def get_crypt_dictionary(keys, value_generator):
    """ (list,function) -> dict
    Returns a dictionary with keys from keys list, value for each key should be\
    obtained by calling the value_generator function.
    
    >>> random.seed(9001)
    >>> a = get_crypt_dictionary(['a', 'b', 'c'], coin_utils.get_random_comp202coin)
    >>> a == {'a': '0c0MPNN0OC', 'b': '0cMIMNIO0P', 'c': '0cM0OCCIOI'}
    True
    
    >>> b = get_crypt_dictionary(['d', 'e'], coin_utils.get_random_comp202coin)
    >>> b == {'d': '0cC0PIIMCP', 'e': '0cM00N22O2'}
    True
    
    >>> c = get_crypt_dictionary([], coin_utils.get_random_comp202coin)
    >>> c == {}
    True
    
    >>> d = get_crypt_dictionary(('a', 'b'), coin_utils.get_random_comp202coin)
    Traceback (most recent call last):
    AssertionError: The input should be a list and a function
    
    >>> e = get_crypt_dictionary(['a', 'b', 'a'], coin_utils.get_random_comp202coin)
    Traceback (most recent call last):
    AssertionError: duplicate keys found
    
    >>> f = get_crypt_dictionary(['a', 'b', 'c'], 'get_random_comp202coin')
    Traceback (most recent call last):
    AssertionError: The input should be a list and a function
    """
    #raise AssertionError if the input type is not correct
    if type(keys) != list or str(type(value_generator)) != "<class 'function'>":
        raise AssertionError("The input should be a list and a function")
    
    #raise AssertionError if duplicate keys in keys list
    unique_keys = coin_utils.get_unique_elements(keys)
    if len(unique_keys) != len(keys):
        raise AssertionError("duplicate keys found")
        
    
    #creates a new dictionary to add items on, a new list to add on value generated
    crypt_dictionary = dict()
    value_list = []
    
    for index in range(len(keys)):
        #generate value for key by calling value_generator
        value = value_generator(index)
        
        #if value generated have already added to the dictionary, generate again
        while value in value_list:
            value = value_generator(index)
    
        #add a new item to crypt_dictionary
        crypt_dictionary[keys[index]] = value
        
        value_list.append(value)
        
    return crypt_dictionary
    
    

def encrypt_text(text):
    """ (str) -> (str,dict)
    Returns the encrypted string and encryption dictionary as a tuple,
    which the function encrypt the string into COMP202COIN.
    
    >>> random.seed(9001)
    >>> s, d = encrypt_text('too')
    >>> s == '0c0MPNN0OC-0cMIMNIO0P-0cMIMNIO0P'
    True
    >>> d == {'t': '0c0MPNN0OC', 'o': '0cMIMNIO0P'}
    True
    
    >>> random.seed(9001)
    >>> s, d = encrypt_text("I learned a lot from COMP202, feel excited.")
    >>> len(d)
    19
    >>> d['i']
    '0c0MPNN0OC'
    >>> d['.']
    '0cMN0NPMMM'
    
    >>> random.seed(9001)
    >>> s, d = encrypt_text("This is a language just discovered:egau+fiubejd[vsvd)'cd/24")
    >>> len(d)
    27
    >>> d['[']
    '0cI2COIPIN'
    >>> d[' ']
    '0cM00N22O2'
    
    >>> s, d = encrypt_text("你好")
    Traceback (most recent call last):
    AssertionError: Character not presented in ALL_CHARACTERS found
    """
    #lowercase all characters
    text = text.lower()
    
    #raise AssertionError if the input string contains character not in ALL_CHARACTER
    for char in text:
        if char not in coin_utils.ALL_CHARACTERS:
            print(char)
            raise AssertionError("Character not presented in ALL_CHARACTERS found")
        

    #get a keys list containing all unique character of text 
    char_list = list(text)
    keys = coin_utils.get_unique_elements(char_list)

    #generate an encryption dictionary, keys are each unique character of text
    encryption_dict = get_crypt_dictionary(keys, coin_utils.get_random_comp202coin)
    
    
    #turn each character of the original string into a COMP202COIN, separate by a hyphen
    encrypted_str_list = []
    for char in text:
        encrypted_str_list.append(encryption_dict[char])
        
    #get new string contains all elements in encrypted_str_list, separate by a hyphen
    encrypted_str = '-'.join(encrypted_str_list)
    
    return (encrypted_str, encryption_dict)
        
    

def encrypt_file(filename):
    """ (str) -> dict
    Returns the encryption dictionary used to encrypy the content in the file at filename,
    stores the encrypted contents into a new file.
    
    >>> random.seed(42)
    >>> a = encrypt_file('dubliners.txt')
    >>> len(a)
    64
    >>> a == {'t': '0cCI200CM2', 'h': '0c0OCMN0IP', 'e': '0cMOCP02MM', ' ': '0cON2ICCIN',\
    'p': '0cOMMMM2PP', 'r': '0c2CIN0I0O', 'o': '0cCP0NP0NN', 'j': '0cCOC0CMNN',\
    'c': '0cII00O0MO', 'g': '0c0M0M2N2C', 'u': '0c0OIM0I2M', 'n': '0cCONNMO22',\
    'b': '0cOONN0P2C', 'k': '0cOPICNP2M', 'f': '0c0OOCO0ON', 'd': '0cOCOMN0CM',\
    'l': '0cIPPMPPCP', 'i': '0cOMCPII2N', 's': '0cNCONN2N2', ',': '0cMOMINM0O',\
    'y': '0c00IPCNCI', 'a': '0c2MOONOOP', 'm': '0cII0I0OP2', '\\n': '0cPOMO2P20',\
    'w': '0cMOMM2MMN', 'v': '0c2ONCPM02', '.': '0cOOMOIIO2', '-': '0cPO0PO0OI',\
    ':': '0cCP0P2OMN', '2': '0cCOINICM2', '0': '0cI0P02N2M', '1': '0cCMO02OCN',\
    '[': '0cPPNMI0MP', '#': '0cPM0CPOII', '8': '0cMCIINP0N', '4': '0c0PMONMM2',\
    ']': '0cN2IOMINM', '9': '0cCNNIMMII', '*': '0cI0OMNP02', 'z': '0cC20PMCNN',\
    '(': '0cMPMCPPII', ')': '0cPI22M0NC', 'q': '0cO0MNCIMI', '"': '0cC0NCI2NO',\
    "'": '0c0PINOCCO', 'x': '0cOPC2NM2P', '!': '0cMP02P2P0', ';': '0cC2CPPCNI',\
    '?': '0cOPIO0COP', '_': '0cCMNOOCIP', '5': '0cI0PCNNMN', 'é': '0cMOMPC2CI',\
    'è': '0cN2022PMP', 'ç': '0cPIPMPPC0', '&': '0c2MIMOPMP', 'æ': '0cPNO0MCOM',\
    '7': '0cPPOIO0C2', '6': '0cO2IM220C', 'œ': '0cM2CO0P2C', '/': '0cCCC0NOOI',\
    '3': '0c2PNCNPNM', '%': '0cON2PONOO', '@': '0c2MN2MPNP', '$': '0cNOC2IPOI'}
    True
    >>> fobj = open('dubliners_encrypted.txt', 'r', encoding = 'utf-8')
    >>> len(fobj.read())
    4282475
    
    >>> random.seed(1229)
    >>> b = encrypt_file('common_words.txt')
    >>> len(b)
    23
    >>> b == {'m': '0c2022C0OC', 'e': '0cIN22ONCP', '\\n': '0cCP2IONPC',\
    'y': '0cM02MN2PN','s': '0cP2MOPMPP', 'l': '0c2M2I2C0I', 'f': '0c2NMCIP2C',\
    'w': '0cPMI020MO','o': '0cCMCO0I22', 'u': '0cPP002COO', 'r': '0cI2N0022C',\
    'v': '0c0IPIMNM2','h': '0cNCMMP2N0', 'i': '0c2C2MCIMO', 't': '0cMPINPPOP',\
    'a': '0cPI2CNPPM','c': '0c2N0I2POC', 'b': '0cN0COICPI', 'n': '0cIP2M2IPO',\
    'g': '0cI220I0C2','d': '0cNPPPM0IO', 'p': '0cI0IOIMON', 'j': '0c2NMOPO0M'}
    True
    >>> fobj = open('common_words_encrypted.txt', 'r', encoding = 'utf-8')
    >>> len(fobj.read())
    6753
    
    >>> random.seed(1206)
    >>> d = encrypt_file('dubliners.txt')
    >>> d['t']
    '0cP2ICMP2O'
    >>> d['œ']
    '0c2NO2CONP'
    
    >>> c = encrypt_file(1234)
    Traceback (most recent call last):
    AssertionError: The input should be a string of filename.
    """
    if type(filename) != str:
        raise AssertionError("The input should be a string of filename.")
    
    
    #reads in the contents of the file at the given filename, close the file
    file_object = open(filename, "r", encoding = 'utf-8')
    file_content = file_object.read()
    file_object.close()
    
    #encrypts the file_content
    encrypted_str, encryption_dict = encrypt_text(file_content)
    
    #stores the encrypted contents into a new file
    filename_list = filename.split('.')
    new_file_object = open(filename_list[0]+'_encrypted.'+filename_list[1],\
                           'w',encoding = 'utf-8')
    new_file_object.write(encrypted_str)
    new_file_object.close()
    
    return encryption_dict
    
    

def decrypt_text(text, decryption_dict):
    """ (str,dict) -> str
    Returns the decrypted string using the decryption_dictionary.
    
    >>> a = {'0c0MPNN0OC': 'a', '0cMIMNIO0P': 'b', '0cM0OCCIOI': 'c'}
    >>> decrypt_text('0c0MPNN0OC-0cM0OCCIOI-0c0MPNN0OC', a)
    'aca'
    
    >>> b = {'0c0MPNN0OC': 't', '0cMIMNIO0P': 'o'}
    >>> decrypt_text('0c0MPNN0OC-0cMIMNIO0P-0cMIMNIO0P', b)
    'too'
    
    >>> x = {'0c0MPNN0OC': 'b', '0cMIMNIO0P': 'a', '0cM0OCCIOI': 'n'}
    >>> decrypt_text('0c0MPNN0OC-0cMIMNIO0P-0cM0OCCIOI-0cMIMNIO0P-0cM0OCCIOI-0cMIMNIO0P',\
                      x)
    'banana'
    
    >>> c = {'0cCCCCCCCC': 'a'}
    >>> decrypt_text('hi0cCCCCCCCChi', c)
    Traceback (most recent call last):
    AssertionError: The input string should contain text encrypted in COMP202COIN.
    
    >>> d = {'0c0MPNN0OC': 'a', '0cMIMNIO0P': 'b'}
    >>> decrypt_text('0c0MPNN0OC-0cM0OCCIOI-0c0MPNN0OC', d)
    Traceback (most recent call last):
    AssertionError: The input dictionary should contain COMP202COIN in text as keys.
    """
    #raise AssertionError if the input string is not valid text encrypted in COMP202COIN
    if type(text) != str:
        raise AssertionError("The input string should contain text encrypted in COMP202COIN.")
    
    coins_list = text.split('-')
    for element in coins_list:
        if not is_base202(element):
            raise AssertionError("The input string should contain text encrypted in COMP202COIN.")
    
    
    #raise AssertionError if the input dictionary does not contain all comp202coin\
    #as keys in text, or does not contain decrypted characters as value
    if type(decryption_dict) != dict:
        raise AssertionError("The input dictionary should contain COMP202COIN in text as keys.")
    
    for element in coins_list:
        if element not in decryption_dict:
            raise AssertionError("The input dictionary should contain COMP202COIN in text as keys.")
        
    
    #decrypt the string using the dictionary
    decrypted_string = ""
    for element in coins_list:
        decryped_char = decryption_dict[element]
        decrypted_string += decryped_char
        
    return decrypted_string
    
    
    
def decrypt_file(filename, decryption_dict):
    """ (str,dict) -> NoneType
    Decryped contents of file at filename, stores the decrypted contents into a new file.
    
    >>> decrypt_file('dubliners_encrypted.txt',\
                     coin_utils.reverse_dict(encrypt_file('dubliners.txt')))
    >>> fobj = open('dubliners.txt', 'r', encoding = 'utf=8')
    >>> fobj2 = open('dubliners_encrypted_decrypted.txt', 'r', encoding = 'utf-8')
    >>> fobj.read().lower() == fobj2.read()
    True
    
    >>> decrypt_file('common_words_encrypted.txt',\
                     coin_utils.reverse_dict(encrypt_file('common_words.txt')))
    >>> fobj3 = open('common_words.txt', 'r', encoding = 'utf=8')
    >>> fobj4 = open('common_words_encrypted_decrypted.txt', 'r', encoding = 'utf-8')
    >>> fobj3.read().lower() == fobj4.read()
    True
    
    >>> decrypt_file('testing_encrypted.txt',\
                     coin_utils.reverse_dict(encrypt_file('testing.txt')))
    >>> fobj5 = open('testing.txt', 'r', encoding = 'utf=8')
    >>> fobj6 = open('testing_encrypted_decrypted.txt', 'r', encoding = 'utf-8')
    >>> fobj5.read().lower() == fobj6.read()
    True
    
    >>> decrypt_file(['dubliners_encrypted.txt'],\
                     coin_utils.reverse_dict(encrypt_file('dubliners.txt')))
    Traceback (most recent call last):
    AssertionError: The input should be a string and a dictionary.
    
    >>> decrypt_file('dubliners_encrypted.txt', 'dubliners.txt')
    Traceback (most recent call last):
    AssertionError: The input should be a string and a dictionary.
    """
    #raise AssertionError if any of the input is not correct
    if type(filename) != str or type(decryption_dict) != dict:
        raise AssertionError("The input should be a string and a dictionary.")
    
    
    #reads in the contents of the file at given filename
    file_object = open(filename, 'r', encoding = 'utf-8')
    file_content = file_object.read()
    file_object.close()
    
    #decrypts the file_content using decryption_dict
    decrypt_content = decrypt_text(file_content, decryption_dict)
    
    #stores the decrypted contents into a new file
    filename_list = filename.split('.')
    new_file_object = open(filename_list[0]+"_decrypted."+filename_list[1],'w',\
                           encoding='utf-8')
    new_file_object.write(decrypt_content)
    new_file_object.close()
    
    
    
def random_decrypt(encrypted_s, n, common_words_filename):
    """ (str,int,str) -> str
    Returns the best possible decryption by decrypt encrypted_s string n times,
    measured by the percentage of characters in decrypted string belonging to common words.
    
    >>> random.seed(49)
    >>> encrypted_s = '0c0MPNN0OC-0cMIMNIO0P-0cMIMNIO0P'
    >>> random_decrypt(encrypted_s, 10**2, 'common_words.txt')
    'f33'
    
    >>> random_decrypt(encrypted_s, 10**3, 'common_words.txt')
    'too'
    
    >>> random.seed(1229)
    >>> encrypted_s = '0c0MPNN0OC-0cMIMNIO0P-0cMIMNIO0P'
    >>> random_decrypt(encrypted_s, 10**2, 'common_words.txt')
    '/{{'
    
    >>> random.seed(1206)
    >>> encrypted_s = '0c0MPNN0OC-0cMIMNIO0P-0cM0OCCIOI-0cMIMNIO0P-0cM0OCCIOI-0cMIMNIO0P'
    >>> random_decrypt(encrypted_s, 10**3, 'common_words.txt')
    'pn2n2n'
    
    >>> encrypted_s = 1234
    >>> random_decrypt(encrypted_s, 10**3, 'common_words.txt')
    Traceback (most recent call last):
    AssertionError: The input should be a string, an integer, and a string.
    
    >>> encrypted_s = '0c0MPNN0OC-0cMIMNIO0P-0cMIMNIO0P'
    >>> random_decrypt(encrypted_s, '10**5', 'common_words.txt')
    Traceback (most recent call last):
    AssertionError: The input should be a string, an integer, and a string.
    
    >>> encrypted_s = '0c0MPNN0OC-0cMIMNIO0P-0cMIMNIO0P'
    >>> random_decrypt(encrypted_s, 10**5, ['common_words.txt'])
    Traceback (most recent call last):
    AssertionError: The input should be a string, an integer, and a string.
    
    >>> encrypted_s = 'I love comp202.'
    >>> random_decrypt(encrypted_s, 10**5, 'common_words.txt')
    Traceback (most recent call last):
    AssertionError: The first input contains no COMP202COIN.
    
    >>> encrypted_s = '0c0MPNN0OC-0cMIMNIO0P-0cMIMNIO0P'
    >>> random_decrypt(encrypted_s, 0, ['common_words.txt'])
    Traceback (most recent call last):
    AssertionError: The input should be a string, an integer, and a string.
    """
    #raise AssertionError if ant of the input is not the correct type
    if type(encrypted_s) != str or type(n) != int or type(common_words_filename) != str:
        raise AssertionError("The input should be a string, an integer, and a string.")
    
    if len(coin_utils.get_all_coins(encrypted_s)) == 0:
        raise AssertionError("The first input contains no COMP202COIN.")
    
    if n == 0:
        raise AssertionError("The second input should be a positive integer.")
    
    
    #set highest percentage to 0 to compare, and initiate highest percentage string 
    highest_pct = 0
   
    #decrypt the former string n times,
    while n > 0:
        #a new decryption dictionary is generated 
        keys = coin_utils.get_unique_elements(encrypted_s.split('-'))
        decryption_dict = get_crypt_dictionary(keys, coin_utils.get_random_character)
        
        #decrypt encrypted_s using decryption_dict
        decrypted_str = decrypt_text(encrypted_s, decryption_dict)
        
        #get the percentage of characters in decrypted_str belonging to common words
        pct_common_words = coin_utils.get_pct_common_words(decrypted_str,\
                                                         common_words_filename)
        
        #get the highest percentage of characters, if same percentage, get the last string
        if pct_common_words >= highest_pct:
            highest_pct_str = decrypted_str
            highest_pct = pct_common_words
       
        n -= 1

    
    return highest_pct_str
        
   

def decrypt_with_user_input(encrypted_s):
    """ (str) -> NoneType
    Tries to decrypt encrypted_s by relying both on user's input and on the premise that,
    encrypted_s has a letter frequency standard to the English language.
    
    >> random.seed(0)
    >> s, d = encrypt_text("As I walked along in the sun I remembered old Cotter's\
    words and tried to remember what had happened afterwards in the dream. I remembered\
    that I had noticed long velvet curtains and a swinging lamp of antique\
    fashion. I felt that I had been very far away, in some land where the\
    customs were strange-in Persia, I thought.... But I could not remember\
    the end of the dream.")
    >> s = decrypt_with_user_input(s)
    Decrypted string: OH N YOD"EL ODSRC NR TIE HGR N AEMEMWEAEL SDL USTTEA.H\
    YSALH ORL TANEL TS AEMEMWEA YIOT IOL IOBBEREL OPTEAYOALH NR TIE LAEOMF N AEMEMWEAEL\
    TIOT N IOL RSTNUEL DSRC VEDVET UGATONRH ORL O HYNRCNRC DOMB SP ORTN,GE    POHINSRF\
    N PEDT TIOT N IOL WEER VEAX POA OYOXK NR HSME DORL YIEAE TIE    UGHTSMH YEAE\
    HTAORCE'NR BEAHNOK N TISGCITFFFF WGT N USGDL RST AEMEMWEA    TIE ERL SP TIE LAEOMF\
    End decryption? n
    Enter first letter to swap: H
    Enter second letter to swap: O
    Decrypted string: HO N YHD"EL HDSRC NR TIE OGR N AEMEMWEAEL SDL USTTEA.O\
    YSALO HRL TANEL TS AEMEMWEA YIHT IHL IHBBEREL HPTEAYHALO NR TIE LAEHMF N AEMEMWEAEL\
    TIHT N IHL RSTNUEL DSRC VEDVET UGATHNRO HRL H OYNRCNRC DHMB SP HRTN,GE    PHOINSRF\
    N PEDT TIHT N IHL WEER VEAX PHA HYHXK NR OSME DHRL YIEAE TIE    UGOTSMO YEAE\
    OTAHRCE'NR BEAONHK N TISGCITFFFF WGT N USGDL RST AEMEMWEA    TIE ERL SP TIE LAEHMF
    End decryption? yes
    
    >> random.seed(1229)
    >> s, d = encrypt_text("But no. When we rose and went up to the head of the bed\
    I saw that he was not smiling.")
    >> s = decrypt_with_user_input(s)
    Decrypted string: YHO TLD RAET RE PLIE NTM RETO HC OL OAE AENM LF OAE YEM\
    S INR OANO AE RNI TLO IGSWSTUD
    End decryption?
    Enter first letter to swap: P
    Enter second letter to swap: Y
    Decrypted string: PHO TLD RAET RE YLIE NTM RETO HC OL OAE AENM LF OAE PEM\
    S INR OANO AE RNI TLO IGSWSTUD
    End decryption? yes
    
    >> random.seed(1229)
    >> s, d = encrypt_text("There was a heavy odour in the room-the flowers.")
    >> s = decrypt_with_user_input(s)
    Decrypted string: NAETE IRL R AERCS OUOHT PY NAE TOOMWNAE DFOIETLG
    End decryption? yes

    >> decrypt_with_user_input(1234)
    Traceback (most recent call last):
    AssertionError: The input should be a string.
    """
    #raise AssertionError if the input is not a string
    if type(encrypted_s) != str:
        raise AssertionError("The input should be a string.")
    
    
    #create a list contains all unique coins present in encrypted_s
    coins = coin_utils.get_all_coins(encrypted_s)
    
    #create a dictionary of coins with its frequency, sort the dictionary to a list
    coins_frequency = coin_utils.get_frequencies(coins)
    coins_frequency_descending = coin_utils.sort_keys_by_values(coins_frequency)
    unique_coins = coin_utils.get_unique_elements(coins_frequency_descending)
    
    #create a list contains all values being a char in LETTER_IN_POPUlARITY_ORDER
    values_list = []
    for index in range(len(unique_coins)):
        values_list.append(coin_utils.get_letter_of_popularity_order(index))
        
        
    #create a decryption dictionary
    decryption_dict = dict()
    for i in range(len(unique_coins)):
        decryption_dict[unique_coins[i]] = values_list[i]
        

    #decrypt encrypt_s with decryption_dict
    decrypted_str = decrypt_text(encrypted_s, decryption_dict)
    
    #print the decrypted string to the screen
    print("Decrypted string: " + decrypted_str)
        
    #ask the user to stop or not, if not, ask them for two letters to swap
    answer = input("End decryption? ")
    while answer != "yes":
        letter1 = input("Enter first letter to swap: ")
        letter2 = input("Enter second letter to swap: ")
        
        #swap the two letters input in decrypted_str
        decrypted_str = coin_utils.swap_letters(decrypted_str, letter1, letter2)
        
        print("Decrypted string: " + decrypted_str)
        answer = input("End decryption? ")
        
    
    return 


    
    
if __name__ == "__main__":
    doctest.testmod()
    
#This program manipulate comp202coin by encrypt and decrypt it
#Ziwei Hu 260889365 
import coin_utils
from coins import *
import random
import doctest
 
 
def get_crypt_dictionary(keys, value_generator):
    """ (list,function) -> dict
    Returns a dictionary with keys from keys list, value for each key should be\
    obtained by calling the value_generator function.
    
    >>> random.seed(9001)
    >>> a = get_crypt_dictionary(['a', 'b', 'c'], coin_utils.get_random_comp202coin)
    >>> a == {'a': '0c0MPNN0OC', 'b': '0cMIMNIO0P', 'c': '0cM0OCCIOI'}
    True
    
    >>> b = get_crypt_dictionary(['d', 'e'], coin_utils.get_random_comp202coin)
    >>> b == {'d': '0cC0PIIMCP', 'e': '0cM00N22O2'}
    True
    
    >>> c = get_crypt_dictionary([], coin_utils.get_random_comp202coin)
    >>> c == {}
    True
    
    >>> d = get_crypt_dictionary(('a', 'b'), coin_utils.get_random_comp202coin)
    Traceback (most recent call last):
    AssertionError: The input should be a list and a function
    
    >>> e = get_crypt_dictionary(['a', 'b', 'a'], coin_utils.get_random_comp202coin)
    Traceback (most recent call last):
    AssertionError: duplicate keys found
    
    >>> f = get_crypt_dictionary(['a', 'b', 'c'], 'get_random_comp202coin')
    Traceback (most recent call last):
    AssertionError: The input should be a list and a function
    """
    #raise AssertionError if the input type is not correct
    if type(keys) != list or str(type(value_generator)) != "<class 'function'>":
        raise AssertionError("The input should be a list and a function")
    
    #raise AssertionError if duplicate keys in keys list
    unique_keys = coin_utils.get_unique_elements(keys)
    if len(unique_keys) != len(keys):
        raise AssertionError("duplicate keys found")
        
    
    #creates a new dictionary to add items on, a new list to add on value generated
    crypt_dictionary = dict()
    value_list = []
    
    for index in range(len(keys)):
        #generate value for key by calling value_generator
        value = value_generator(index)
        
        #if value generated have already added to the dictionary, generate again
        while value in value_list:
            value = value_generator(index)
    
        #add a new item to crypt_dictionary
        crypt_dictionary[keys[index]] = value
        
        value_list.append(value)
        
    return crypt_dictionary
    
    
 
def encrypt_text(text):
    """ (str) -> (str,dict)
    Returns the encrypted string and encryption dictionary as a tuple,
    which the function encrypt the string into COMP202COIN.
    
    >>> random.seed(9001)
    >>> s, d = encrypt_text('too')
    >>> s == '0c0MPNN0OC-0cMIMNIO0P-0cMIMNIO0P'
    True
    >>> d == {'t': '0c0MPNN0OC', 'o': '0cMIMNIO0P'}
    True
    
    >>> random.seed(9001)
    >>> s, d = encrypt_text("I learned a lot from COMP202, feel excited.")
    >>> len(d)
    19
    >>> d['i']
    '0c0MPNN0OC'
    >>> d['.']
    '0cMN0NPMMM'
    
    >>> random.seed(9001)
    >>> s, d = encrypt_text("This is a language just discovered:egau+fiubejd[vsvd)'cd/24")
    >>> len(d)
    27
    >>> d['[']
    '0cI2COIPIN'
    >>> d[' ']
    '0cM00N22O2'
    
    >>> s, d = encrypt_text("你好")
    Traceback (most recent call last):
    AssertionError: Character not presented in ALL_CHARACTERS found
    """
    #lowercase all characters
    text = text.lower()
    
    #raise AssertionError if the input string contains character not in ALL_CHARACTER
    for char in text:
        if char not in coin_utils.ALL_CHARACTERS:
            print(char)
            raise AssertionError("Character not presented in ALL_CHARACTERS found")
        
 
    #get a keys list containing all unique character of text 
    char_list = list(text)
    keys = coin_utils.get_unique_elements(char_list)
 
    #generate an encryption dictionary, keys are each unique character of text
    encryption_dict = get_crypt_dictionary(keys, coin_utils.get_random_comp202coin)
    
    
    #turn each character of the original string into a COMP202COIN, separate by a hyphen
    encrypted_str_list = []
    for char in text:
        encrypted_str_list.append(encryption_dict[char])
        
    #get new string contains all elements in encrypted_str_list, separate by a hyphen
    encrypted_str = '-'.join(encrypted_str_list)
    
    return (encrypted_str, encryption_dict)
        
    
 
def encrypt_file(filename):
    """ (str) -> dict
    Returns the encryption dictionary used to encrypy the content in the file at filename,
    stores the encrypted contents into a new file.
    
    >>> random.seed(42)
    >>> a = encrypt_file('dubliners.txt')
    >>> len(a)
    64
    >>> a == {'t': '0cCI200CM2', 'h': '0c0OCMN0IP', 'e': '0cMOCP02MM', ' ': '0cON2ICCIN',\
    'p': '0cOMMMM2PP', 'r': '0c2CIN0I0O', 'o': '0cCP0NP0NN', 'j': '0cCOC0CMNN',\
    'c': '0cII00O0MO', 'g': '0c0M0M2N2C', 'u': '0c0OIM0I2M', 'n': '0cCONNMO22',\
    'b': '0cOONN0P2C', 'k': '0cOPICNP2M', 'f': '0c0OOCO0ON', 'd': '0cOCOMN0CM',\
    'l': '0cIPPMPPCP', 'i': '0cOMCPII2N', 's': '0cNCONN2N2', ',': '0cMOMINM0O',\
    'y': '0c00IPCNCI', 'a': '0c2MOONOOP', 'm': '0cII0I0OP2', '\\n': '0cPOMO2P20',\
    'w': '0cMOMM2MMN', 'v': '0c2ONCPM02', '.': '0cOOMOIIO2', '-': '0cPO0PO0OI',\
    ':': '0cCP0P2OMN', '2': '0cCOINICM2', '0': '0cI0P02N2M', '1': '0cCMO02OCN',\
    '[': '0cPPNMI0MP', '#': '0cPM0CPOII', '8': '0cMCIINP0N', '4': '0c0PMONMM2',\
    ']': '0cN2IOMINM', '9': '0cCNNIMMII', '*': '0cI0OMNP02', 'z': '0cC20PMCNN',\
    '(': '0cMPMCPPII', ')': '0cPI22M0NC', 'q': '0cO0MNCIMI', '"': '0cC0NCI2NO',\
    "'": '0c0PINOCCO', 'x': '0cOPC2NM2P', '!': '0cMP02P2P0', ';': '0cC2CPPCNI',\
    '?': '0cOPIO0COP', '_': '0cCMNOOCIP', '5': '0cI0PCNNMN', 'é': '0cMOMPC2CI',\
    'è': '0cN2022PMP', 'ç': '0cPIPMPPC0', '&': '0c2MIMOPMP', 'æ': '0cPNO0MCOM',\
    '7': '0cPPOIO0C2', '6': '0cO2IM220C', 'œ': '0cM2CO0P2C', '/': '0cCCC0NOOI',\
    '3': '0c2PNCNPNM', '%': '0cON2PONOO', '@': '0c2MN2MPNP', '$': '0cNOC2IPOI'}
    True
    >>> fobj = open('dubliners_encrypted.txt', 'r', encoding = 'utf-8')
    >>> len(fobj.read())
    4282475
    
    >>> random.seed(1229)
    >>> b = encrypt_file('common_words.txt')
    >>> len(b)
    23
    >>> b == {'m': '0c2022C0OC', 'e': '0cIN22ONCP', '\\n': '0cCP2IONPC',\
    'y': '0cM02MN2PN','s': '0cP2MOPMPP', 'l': '0c2M2I2C0I', 'f': '0c2NMCIP2C',\
    'w': '0cPMI020MO','o': '0cCMCO0I22', 'u': '0cPP002COO', 'r': '0cI2N0022C',\
    'v': '0c0IPIMNM2','h': '0cNCMMP2N0', 'i': '0c2C2MCIMO', 't': '0cMPINPPOP',\
    'a': '0cPI2CNPPM','c': '0c2N0I2POC', 'b': '0cN0COICPI', 'n': '0cIP2M2IPO',\
    'g': '0cI220I0C2','d': '0cNPPPM0IO', 'p': '0cI0IOIMON', 'j': '0c2NMOPO0M'}
    True
    >>> fobj = open('common_words_encrypted.txt', 'r', encoding = 'utf-8')
    >>> len(fobj.read())
    6753
    
    >>> random.seed(1206)
    >>> d = encrypt_file('dubliners.txt')
    >>> d['t']
    '0cP2ICMP2O'
    >>> d['œ']
    '0c2NO2CONP'
    
    >>> c = encrypt_file(1234)
    Traceback (most recent call last):
    AssertionError: The input should be a string of filename.
    """
    if type(filename) != str:
        raise AssertionError("The input should be a string of filename.")
    
    
    #reads in the contents of the file at the given filename, close the file
    file_object = open(filename, "r", encoding = 'utf-8')
    file_content = file_object.read()
    file_object.close()
    
    #encrypts the file_content
    encrypted_str, encryption_dict = encrypt_text(file_content)
    
    #stores the encrypted contents into a new file
    filename_list = filename.split('.')
    new_file_object = open(filename_list[0]+'_encrypted.'+filename_list[1],\
                           'w',encoding = 'utf-8')
    new_file_object.write(encrypted_str)
    new_file_object.close()
    
    return encryption_dict
    
    
 
def decrypt_text(text, decryption_dict):
    """ (str,dict) -> str
    Returns the decrypted string using the decryption_dictionary.
    
    >>> a = {'0c0MPNN0OC': 'a', '0cMIMNIO0P': 'b', '0cM0OCCIOI': 'c'}
    >>> decrypt_text('0c0MPNN0OC-0cM0OCCIOI-0c0MPNN0OC', a)
    'aca'
    
    >>> b = {'0c0MPNN0OC': 't', '0cMIMNIO0P': 'o'}
    >>> decrypt_text('0c0MPNN0OC-0cMIMNIO0P-0cMIMNIO0P', b)
    'too'
    
    >>> x = {'0c0MPNN0OC': 'b', '0cMIMNIO0P': 'a', '0cM0OCCIOI': 'n'}
    >>> decrypt_text('0c0MPNN0OC-0cMIMNIO0P-0cM0OCCIOI-0cMIMNIO0P-0cM0OCCIOI-0cMIMNIO0P',\
                      x)
    'banana'
    
    >>> c = {'0cCCCCCCCC': 'a'}
    >>> decrypt_text('hi0cCCCCCCCChi', c)
    Traceback (most recent call last):
    AssertionError: The input string should contain text encrypted in COMP202COIN.
    
    >>> d = {'0c0MPNN0OC': 'a', '0cMIMNIO0P': 'b'}
    >>> decrypt_text('0c0MPNN0OC-0cM0OCCIOI-0c0MPNN0OC', d)
    Traceback (most recent call last):
    AssertionError: The input dictionary should contain COMP202COIN in text as keys.
    """
    #raise AssertionError if the input string is not valid text encrypted in COMP202COIN
    if type(text) != str:
        raise AssertionError("The input string should contain text encrypted in COMP202COIN.")
    
    coins_list = text.split('-')
    for element in coins_list:
        if not is_base202(element):
            raise AssertionError("The input string should contain text encrypted in COMP202COIN.")
    
    
    #raise AssertionError if the input dictionary does not contain all comp202coin\
    #as keys in text, or does not contain decrypted characters as value
    if type(decryption_dict) != dict:
        raise AssertionError("The input dictionary should contain COMP202COIN in text as keys.")
    
    for element in coins_list:
        if element not in decryption_dict:
            raise AssertionError("The input dictionary should contain COMP202COIN in text as keys.")
        
    
    #decrypt the string using the dictionary
    decrypted_string = ""
    for element in coins_list:
        decryped_char = decryption_dict[element]
        decrypted_string += decryped_char
        
    return decrypted_string
    
    
    
def decrypt_file(filename, decryption_dict):
    """ (str,dict) -> NoneType
    Decryped contents of file at filename, stores the decrypted contents into a new file.
    
    >>> decrypt_file('dubliners_encrypted.txt',\
                     coin_utils.reverse_dict(encrypt_file('dubliners.txt')))
    >>> fobj = open('dubliners.txt', 'r', encoding = 'utf=8')
    >>> fobj2 = open('dubliners_encrypted_decrypted.txt', 'r', encoding = 'utf-8')
    >>> fobj.read().lower() == fobj2.read()
    True
    
    >>> decrypt_file('common_words_encrypted.txt',\
                     coin_utils.reverse_dict(encrypt_file('common_words.txt')))
    >>> fobj3 = open('common_words.txt', 'r', encoding = 'utf=8')
    >>> fobj4 = open('common_words_encrypted_decrypted.txt', 'r', encoding = 'utf-8')
    >>> fobj3.read().lower() == fobj4.read()
    True
    
    >>> decrypt_file('testing_encrypted.txt',\
                     coin_utils.reverse_dict(encrypt_file('testing.txt')))
    >>> fobj5 = open('testing.txt', 'r', encoding = 'utf=8')
    >>> fobj6 = open('testing_encrypted_decrypted.txt', 'r', encoding = 'utf-8')
    >>> fobj5.read().lower() == fobj6.read()
    True
    
    >>> decrypt_file(['dubliners_encrypted.txt'],\
                     coin_utils.reverse_dict(encrypt_file('dubliners.txt')))
    Traceback (most recent call last):
    AssertionError: The input should be a string and a dictionary.
    
    >>> decrypt_file('dubliners_encrypted.txt', 'dubliners.txt')
    Traceback (most recent call last):
    AssertionError: The input should be a string and a dictionary.
    """
    #raise AssertionError if any of the input is not correct
    if type(filename) != str or type(decryption_dict) != dict:
        raise AssertionError("The input should be a string and a dictionary.")
    
    
    #reads in the contents of the file at given filename
    file_object = open(filename, 'r', encoding = 'utf-8')
    file_content = file_object.read()
    file_object.close()
    
    #decrypts the file_content using decryption_dict
    decrypt_content = decrypt_text(file_content, decryption_dict)
    
    #stores the decrypted contents into a new file
    filename_list = filename.split('.')
    new_file_object = open(filename_list[0]+"_decrypted."+filename_list[1],'w',\
                           encoding='utf-8')
    new_file_object.write(decrypt_content)
    new_file_object.close()
    
    
    
def random_decrypt(encrypted_s, n, common_words_filename):
    """ (str,int,str) -> str
    Returns the best possible decryption by decrypt encrypted_s string n times,
    measured by the percentage of characters in decrypted string belonging to common words.
    
    >>> random.seed(49)
    >>> encrypted_s = '0c0MPNN0OC-0cMIMNIO0P-0cMIMNIO0P'
    >>> random_decrypt(encrypted_s, 10**2, 'common_words.txt')
    'f33'
    
    >>> random_decrypt(encrypted_s, 10**3, 'common_words.txt')
    'too'
    
    >>> random.seed(1229)
    >>> encrypted_s = '0c0MPNN0OC-0cMIMNIO0P-0cMIMNIO0P'
    >>> random_decrypt(encrypted_s, 10**2, 'common_words.txt')
    '/{{'
    
    >>> random.seed(1206)
    >>> encrypted_s = '0c0MPNN0OC-0cMIMNIO0P-0cM0OCCIOI-0cMIMNIO0P-0cM0OCCIOI-0cMIMNIO0P'
    >>> random_decrypt(encrypted_s, 10**3, 'common_words.txt')
    'pn2n2n'
    
    >>> encrypted_s = 1234
    >>> random_decrypt(encrypted_s, 10**3, 'common_words.txt')
    Traceback (most recent call last):
    AssertionError: The input should be a string, an integer, and a string.
    
    >>> encrypted_s = '0c0MPNN0OC-0cMIMNIO0P-0cMIMNIO0P'
    >>> random_decrypt(encrypted_s, '10**5', 'common_words.txt')
    Traceback (most recent call last):
    AssertionError: The input should be a string, an integer, and a string.
    
    >>> encrypted_s = '0c0MPNN0OC-0cMIMNIO0P-0cMIMNIO0P'
    >>> random_decrypt(encrypted_s, 10**5, ['common_words.txt'])
    Traceback (most recent call last):
    AssertionError: The input should be a string, an integer, and a string.
    
    >>> encrypted_s = 'I love comp202.'
    >>> random_decrypt(encrypted_s, 10**5, 'common_words.txt')
    Traceback (most recent call last):
    AssertionError: The first input contains no COMP202COIN.
    
    >>> encrypted_s = '0c0MPNN0OC-0cMIMNIO0P-0cMIMNIO0P'
    >>> random_decrypt(encrypted_s, 0, ['common_words.txt'])
    Traceback (most recent call last):
    AssertionError: The input should be a string, an integer, and a string.
    """
    #raise AssertionError if ant of the input is not the correct type
    if type(encrypted_s) != str or type(n) != int or type(common_words_filename) != str:
        raise AssertionError("The input should be a string, an integer, and a string.")
    
    if len(coin_utils.get_all_coins(encrypted_s)) == 0:
        raise AssertionError("The first input contains no COMP202COIN.")
    
    if n == 0:
        raise AssertionError("The second input should be a positive integer.")
    
    
    #set highest percentage to 0 to compare, and initiate highest percentage string 
    highest_pct = 0
   
    #decrypt the former string n times,
    while n > 0:
        #a new decryption dictionary is generated 
        keys = coin_utils.get_unique_elements(encrypted_s.split('-'))
        decryption_dict = get_crypt_dictionary(keys, coin_utils.get_random_character)
        
        #decrypt encrypted_s using decryption_dict
        decrypted_str = decrypt_text(encrypted_s, decryption_dict)
        
        #get the percentage of characters in decrypted_str belonging to common words
        pct_common_words = coin_utils.get_pct_common_words(decrypted_str,\
                                                         common_words_filename)
        
        #get the highest percentage of characters, if same percentage, get the last string
        if pct_common_words >= highest_pct:
            highest_pct_str = decrypted_str
            highest_pct = pct_common_words
       
        n -= 1
 
    
    return highest_pct_str
        
   
 
def decrypt_with_user_input(encrypted_s):
    """ (str) -> NoneType
    Tries to decrypt encrypted_s by relying both on user's input and on the premise that,
    encrypted_s has a letter frequency standard to the English language.
    
    >> random.seed(0)
    >> s, d = encrypt_text("As I walked along in the sun I remembered old Cotter's\
    words and tried to remember what had happened afterwards in the dream. I remembered\
    that I had noticed long velvet curtains and a swinging lamp of antique\
    fashion. I felt that I had been very far away, in some land where the\
    customs were strange-in Persia, I thought.... But I could not remember\
    the end of the dream.")
    >> s = decrypt_with_user_input(s)
    Decrypted string: OH N YOD"EL ODSRC NR TIE HGR N AEMEMWEAEL SDL USTTEA.H\
    YSALH ORL TANEL TS AEMEMWEA YIOT IOL IOBBEREL OPTEAYOALH NR TIE LAEOMF N AEMEMWEAEL\
    TIOT N IOL RSTNUEL DSRC VEDVET UGATONRH ORL O HYNRCNRC DOMB SP ORTN,GE    POHINSRF\
    N PEDT TIOT N IOL WEER VEAX POA OYOXK NR HSME DORL YIEAE TIE    UGHTSMH YEAE\
    HTAORCE'NR BEAHNOK N TISGCITFFFF WGT N USGDL RST AEMEMWEA    TIE ERL SP TIE LAEOMF\
    End decryption? n
    Enter first letter to swap: H
    Enter second letter to swap: O
    Decrypted string: HO N YHD"EL HDSRC NR TIE OGR N AEMEMWEAEL SDL USTTEA.O\
    YSALO HRL TANEL TS AEMEMWEA YIHT IHL IHBBEREL HPTEAYHALO NR TIE LAEHMF N AEMEMWEAEL\
    TIHT N IHL RSTNUEL DSRC VEDVET UGATHNRO HRL H OYNRCNRC DHMB SP HRTN,GE    PHOINSRF\
    N PEDT TIHT N IHL WEER VEAX PHA HYHXK NR OSME DHRL YIEAE TIE    UGOTSMO YEAE\
    OTAHRCE'NR BEAONHK N TISGCITFFFF WGT N USGDL RST AEMEMWEA    TIE ERL SP TIE LAEHMF
    End decryption? yes
    
    >> random.seed(1229)
    >> s, d = encrypt_text("But no. When we rose and went up to the head of the bed\
    I saw that he was not smiling.")
    >> s = decrypt_with_user_input(s)
    Decrypted string: YHO TLD RAET RE PLIE NTM RETO HC OL OAE AENM LF OAE YEM\
    S INR OANO AE RNI TLO IGSWSTUD
    End decryption?
    Enter first letter to swap: P
    Enter second letter to swap: Y
    Decrypted string: PHO TLD RAET RE YLIE NTM RETO HC OL OAE AENM LF OAE PEM\
    S INR OANO AE RNI TLO IGSWSTUD
    End decryption? yes
    
    >> random.seed(1229)
    >> s, d = encrypt_text("There was a heavy odour in the room-the flowers.")
    >> s = decrypt_with_user_input(s)
    Decrypted string: NAETE IRL R AERCS OUOHT PY NAE TOOMWNAE DFOIETLG
    End decryption? yes
 
    >> decrypt_with_user_input(1234)
    Traceback (most recent call last):
    AssertionError: The input should be a string.
    """
    #raise AssertionError if the input is not a string
    if type(encrypted_s) != str:
        raise AssertionError("The input should be a string.")
    
    
    #create a list contains all unique coins present in encrypted_s
    coins = coin_utils.get_all_coins(encrypted_s)
    
    #create a dictionary of coins with its frequency, sort the dictionary to a list
    coins_frequency = coin_utils.get_frequencies(coins)
    coins_frequency_descending = coin_utils.sort_keys_by_values(coins_frequency)
    unique_coins = coin_utils.get_unique_elements(coins_frequency_descending)
    
    #create a list contains all values being a char in LETTER_IN_POPUlARITY_ORDER
    values_list = []
    for index in range(len(unique_coins)):
        values_list.append(coin_utils.get_letter_of_popularity_order(index))
        
        
    #create a decryption dictionary
    decryption_dict = dict()
    for i in range(len(unique_coins)):
        decryption_dict[unique_coins[i]] = values_list[i]
        
 
    #decrypt encrypt_s with decryption_dict
    decrypted_str = decrypt_text(encrypted_s, decryption_dict)
    
    #print the decrypted string to the screen
    print("Decrypted string: " + decrypted_str)
        
    #ask the user to stop or not, if not, ask them for two letters to swap
    answer = input("End decryption? ")
    while answer != "yes":
        letter1 = input("Enter first letter to swap: ")
        letter2 = input("Enter second letter to swap: ")
        
        #swap the two letters input in decrypted_str
        decrypted_str = coin_utils.swap_letters(decrypted_str, letter1, letter2)
        
        print("Decrypted string: " + decrypted_str)
        answer = input("End decryption? ")
        
    
    return 
 
 
    
    
if __name__ == "__main__":
    doctest.testmod()
    
 