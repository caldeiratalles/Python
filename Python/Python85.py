senha = input()
if (('1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0' in senha)) and (('q' or 'w' or 'e' or 'r' or 't' or 'y' or 'u' or 'i' or 'o' or 'p' or 'a' or 's' or 'd' or 'f' or 'g' or 'h' or 'j' or 'k' or 'l' or 'z' or 'x' or 'c' or 'v' or 'b' or 'n' or 'm' in senha)==True) and (('Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M' in senha)==True) and (len(senha)>=6 and len(senha)<=32) and (senha.isspace()==False) and (('á,é,í,ó,ú,â,ê,ô,à,ã,õ' in senha)==False):
    print('Senha Valida.')
else:
    print('Senha invalida.')