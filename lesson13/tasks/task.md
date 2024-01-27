### Начнем работать с реальными данными! 

Для этого будем писать так называемые парсеры - программы, которые берут на вход источник (текст \ ссылку \ строку), 
созданные по определенному формату, а далее преобразуют информацию из этого источника в удобную для использования 
форму. 

Для этого задания напишите класс для парсинга FASTA файлов - файлов для записи информации о молекулах. 

```FASTA
; comment 1
; comment 2
>MCHU - Calmodulin - Human, rabbit, bovine, rat, and chicken
tgcaccaaacatgtctaaagctggaaccaaaattactttctttgaagacaaaaactttca
aggccgccactatgacagcgattgcgactgtgcagatttccacatgtacctgagccgctg
caactccatcagagtggaaggaggcacctgggctgtgtatgaaaggcccaattttgctgg
gtacatgtacatcctaccccggggcgagtatcctgagtaccagcactggatgggcctcaa
cgaccgcctcagctcctgcagggctgttcacctgtctagtggaggccagtataagcttca
gatctttgagaaaggggattttaatggtcagatgcatgagaccacggaagactgcccttc
catcatggagcagttccacatgcgggaggtccactcctgtaaggtgctggagggcgcctg
gatcttctatgagctgcccaactaccgaggcaggcagtacctgctggacaagaaggagta
ccggaagcccgtcgactggggtgcagcttccccagctgtccagtctttccgccgcattgt
ggagtgatgatacagatgcggccaaacgctggctggccttgtcatccaaataagcattat
aaataaaacaattggcatgc
```

Класс должен иметь метод parse для парсинга файлов и возвращать экземпляр класс, который будет содержать в себе 
последовательность молекул + метаинформацию о них (содержащуюся на строке с >).


Выполните задание по ссылке: https://airtable.com/appP9DyHXriAx6KTA/shraSdUUOqcX9bm7h

