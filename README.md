# Rýmovník

**Rýmovník** je jednoduchý konzolový prográmek pro hledání rýmů ve slovníku slov.

## Použití

**Rýmovník** umožňuje hledání podle 3 kritérií:

1. Hledání konce slov pomocí `-k`.
2. Hledání řetězce kdekoliv ve slově `-s`.
3. Hledání pomocí regulárního výrazu `-r`.
4. Nalezená slova lze omezit na konkrétní délku `-d`.

### Na konci slova

~~~
$ rymovnik -k raj
~~~

vyhledá všechna slova končící na **raj**, například *kraj*, *hraj* a tak podobně.


### Kdekoliv ve slově

~~~
$ rymovnik -s raj
~~~

vyhledá všechna slova, který obsahují **raj**, například *kraj*, *krajina*, *okraj* a tak dále. 


### Hledání pomocí regulárního výrazu

~~~
$ rymovnik -r \\w+ovo\$
~~~

vyhledá všechna slova, který končí na **ovo**. Pro správnou interpretaci regulárního výrazu je nutné jej uvést zpětným lomítkem, například začátek slova se musí napsat jako `\^` a ne jenom `^`. 

### Omezení výsledku na slova určité délky

~~~
$ rymovnik -s raj -d 6
~~~

vyhledá všechna slova, která obsahují řetětec **raj** a mají právě 6 znaků, například *krajta*, *okraje*,

