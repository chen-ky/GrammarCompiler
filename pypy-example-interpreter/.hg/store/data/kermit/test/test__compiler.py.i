         �  {       ����������]��t��+A���Oݷ?�            (�/�`{ % BM*!@K� �#KLj��Є@�>7��!��Ŋ�c������-�� X �$�F�`�$L�Z�b  q��fm���#�#��ўa��/zcpc���Nk�!��N�z�F$)3�HU�G
��h���<�fm��H�T��TZ8�T����N����S�ŧ# 7���T��̙��,��	Dc���2�*��Ů�&�R3��0i�:.���n%�I     �     |  �           ����=��xH�綾ǩ��f3X2��            (�/� �� ��!��3�0�~ˉ��h���=�ڵ���oOf�8`��*pC!�`��� l�d+���z���Ǘ�Cz�6�FQ�������^!��z
�6]<��m��V�=� p �����
��/    j     �  g         ������~m'Յx��E=ym5$� �            (�/� �� 4  �  RETURN 0
  � �
def test_add(self):.check_compile('a + 1;', '''LOAD_VAR 0CONSTANTBINARY_ADDDISCARD_TOP''')

 j��r�Ӡ��)L��4�������������         x  �         ������`�P.��O!����"�            (�/� �} d  g �    def test_print(self):
.check_compile(' a;', '''
  LOAD_VAR 0PRINTRETURN''')
	 4M�i�͒� L��4 �i݃#    �     �  �         ����eX���2 ���J|:_�o!:R            (�/� �� �  � �
    def test_while(self):.check_comp' (1) { print 1; }', '''LOAD_CONSTANT 0JUMP_IF_FALSE 11PRIBACKWARDRETURN''')
 4M�18���⨒OX��5W%�:Q��L`��͍9"    )     �  �         ����N�Ђr�tj����u;OK��            (�/� � �  � �
    def test_if(self):.check_compile('''if (a) {   1;}''', LOAD_VAR 0
JUMP_IF_FALSE 8
CONSTANTDISCARD_TOPRETURN''')
 4M�i�T����+�-��,�f��*�¦��    �     �        "   ����m3/1�j���TϘ8Te�            (�/�`_ � �@�h�YNqa{&��.�hg�5��5x1�5���E���<��b����b��E�,������5>_��A�����iS���Ti��E]j��|���)c��ݎ�uw���  "̀����L7�8�V1�É4�i来�T��X���=8"    {     �  �      #   �����sɵ�!5�N��?����            (�/� �u $  � �    def test_lt_floats(self):
.check_compile('1.5 < .5;', '''LOAD_CONSTANT 01BINARY_LDISCARD_TOPRETURN''')


 4���Oq��֟Ҕi�"(�