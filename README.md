# Arxiv Generator

Ever wanted to have a publish worthy paper without all the work? Well keep dreaming because that won't happen, but here's an attempt at that. Using papers published to Arxiv, I trained a TensorFlow RNN to generate new papers using [Arxiv.py](https://github.com/lukasschwab/arxiv.py) and [tensorflow-shakespeare-poem-generator](https://github.com/burliEnterprises/tensorflow-shakespeare-poem-generator).

## Prerequisites

Arxiv library
```
pip install arxiv
```
TensorFlow (Python3)

[Install guide](https://www.tensorflow.org/install/)

## Usage

### Gather Data
First edit gatherdata.py for your Arxiv needs. You can choose several different ways to select Arxiv papers, first you must pick how you want to search.

| Search Query      | Field Argument |
|-------------------|----------------|
| Title             | ti             |
| Author            | au             |
| Abstract          | abs            |
| Comment           | co             |
| Journal Reference | jr             |
| Subject Category  | cat            |
| Report Number     | rn             |
| Id                | id             |
| All of the above  | all            |

I primarily used Subject Category.

If you're using Subject Category, all possible values can be found on [Arxiv's documentation](https://arxiv.org/help/api/user-manual#subject_classifications). I used Representation Theory.

An example query would be something like
```
paper = arxiv.query(search_query="au"+":"+"Einstein",max_results=100)
```
More on this can be found [here](https://github.com/lukasschwab/arxiv.py) and [official Arxiv documentation](https://arxiv.org/help/api/user-manual)

Now we simply run it

```
python gatherdata.py
```

This should take a while as it must first query each paper and then download them.

### Convert to text file

Each paper must be converted a text file. This was done using a bash script.

```
chmod +x ./PDFtoTEXT.sh
./PDFtoTEXT.sh
```

This will convert the papers and then delete the pdf version. 

### Training

Next we will train our network. Make sure to have VirtualEnv activated.

```
python3 rnn_train.py
```

Prepare to leave this for a while. You can view how the network is learning using TensorBoard.

```
tensorboard --logdir ./log/
```
and then navigate your browser to `localhost:6006`

![TensorBoard Preview](https://github.com/Yemeen/Arxiv-Generator/blob/master/tensorboard.png)

### Generating Text

when you feel that your network has had adequate training you can then run
```
python3 rnn_play.py
```
Output will be visible in your terminal and in `generated_output.txt`


## Generated Excerpts

```

                                                                                                    
                               1             1                      1                       1
                                                                                                    
                                                                                                    
                                                                                       1991.


                                                     11
[10] R. S. Summen, A. Mangel, Reparential of the componint of the commutative subalgebra of a group
 scheme over a field of characteristic p > 0 and G is an irreducible representation of G. The catego
ry of
compact groups over the symmetric group Scheme are independent of the field F . The construction in 
this subgroup of G is a commutative group scheme and an algebraic group of any generator of a field 
of
characteristic z respectively. The set of all subgroups of G and G is an algebra called algebraic gr
oup scheme
as a subgroup sf that for all subgroups of G, and the subspace of smooth modules in the constituent 
of the symmetric group of GL(n) are independent over k. The composition
series of triples of a class of all submodules. In this section and can
be
complete the case of an infinite dimensional Lie group scheme of the symmetric groups and the repres
entation theory of a finite group scheme
                                                                                     

 Proposition 3.2. If  is the components of the set of integers such that ()     . This
is a set of all parabolic subgroups of G , then the first sum is a set of algebras and  are all s
imple subspaces.

 (P ) = P  (P ) = P  (Q : P : P : P 
P : P  P P P P P  P  P P  P P P P P  P   PP .
Proof. Let   P be the subset of M  , then     P  P ,   P  P ,
which is a positive. The following set of
-stable cases the following statement is the set of simple modules are equivalent.
    (i) The set of algebras are denoted by the following proposition is proved.
                                                                                                      
                                                                       .................................
    ...................................................                                          .......
     .. .. ...      .....................                                    . ....  ..                 
               .    .. .................................................................................
    ....................................................................................................
    ....................................................................................................
    .......................................................................... .........................
    ....................... ............................................................................
    ....................... ............................................................................
    ............................... ......................................... ..........................
    ....................................................................................................
    ....................................................................................................
    ................. ..................................................................................
    ... ..... ..................................................... ............... ....................
    ............................. ......................................................................
    ....................... .......................................... ................ ................
    ............................................................................ .....    ...... .......
    ....................................................................................................
    ....................................................................................................
    ............................................................................... ....................
    ................................................................................................... 
    ........ ...........................................................................................
    ....................................................................................................
    .................................................. .................................................
    ....................................................................................................
    ..................................................................................................
    ..................................................................................................
    ..................................................................................................
    .................................................................................................
    ..................................................................................................
    ..................................................................................................
    .................................................................................................
    ...................................................................................................
    ...................................................................................................
    .................................................................................................
    ...................................................................................................
    ...................................................................................................
    ...................................................................................................
    .................................................................................................
    .................................................................................................
    ....................................................................................................
    .................................................................................................
    .................................................................................................
    .................................................................................................
    ..................................................................................................
    ..................................................................................................
    .................................................................................................
    .............................................................................................
    ................................................................................................
    ............................................................................................
    ............................................................................................
    ................................................................................................
    ..............................................................................................
    .................................................................................................
    ...........................................................................................
    ..................................................................................................
    .................................................................................................
    ....................................................................................................
    .................................................................................................
    ...............................................................................................
    ..................................................................................................
    ................................................................................................
    ..................................................................................................
    ................................................................................................
    ...................................................................................................
    ....................................................................................................
    .................................................................................................
    ...........................................................................................
    ........................
                                A.EONDE AND LUE AND LEITES
                                                   
                          .

Proposition 3.1. Let P  P  P  P   P be the canonical bilinear form of  . The following
diagram: ()     ()   (), we have
                                                         
                            (  ) =                                                 
   .

                                                                
    . Let      be the set of all -this expressions from the
factor                . Then
                                                                    
                                                              
                                         
                                                                                
                                                                  
           .
                                                                                                                                        
                                                                                                                                         
                                                                                                                                         
                                            .
                                                                                                                                         
                                                                                                                                         
                                                                                                                                         
                                                            ....
                                                                                                                                         
                                                                                                      .
                                                                                                                                         
                                                                                                                                         
                                                                                   ...
                                                                                                       ..... ......................... ..
                                     ....................................................................................................
                                     ....................................................................................................
                                     ........................... ........ ... ...........................................................
                                     ....................................................................................................
                                     ........................................................................                ....        
                                                                                            ... .... ....................................
                                     ................ ..........................................................                         
                                        .                  . ..... ......      .. ...                                                    
                                                 ... ...            ...                                                  ............    
                                                        .            ......                                                        ......
                                     ..                       ......................                                                     
                                       ........................................................................................ .........
                                     ................ ...................................................................................
                                     ....................... ... ........................................................................
                                     .............          .. .....................................           ..........................
                                     ............................................... ....................................................
                                     ............................... ....................................................................
                                     ....................................................................................................
                                     .............................................................................. .....................
                                     ....................................... ............................................................
                                     ....................................................................................................
                                     ....................................................................................................
                                     ....................................................................................................
                                     ....................................................................................................
                                     . ..................................................................................................
                                     ....................................................................................................
                                     ....................................................................................................
                                     ....................................................................................................
                                     ...................................................................................................
                                     ....................................................................................................
                                     ..................................................................................................
                                     ...................................................................................................
                                     ..................................................................................................
                                     ...................................................................................................
                                     ................................................................................................
                                     ...................................................................................................
                                     ...................................................................................................
                                     ..................................................................................................
                                     ...............................................................................................
                                     ..................................................................................................
                                     ................................................................................................
                                     ..................................................................................................
                                     ...............................................................................................
                                     ..................................................................................................
                                     ..................................................................................................
                                     ..............................................................................................
                                     ..................................................................................................
                                     ...................................................................................................
                                     ....................................................................................................
                                     ...................................................................................................
                                     ...................................................................................................
                                     ...................................................................................................
                                     ....................................................................................................
                                     ................................................................................................
                                     ....................................................................................................
                                     ...............................................................................................
                                     ..................................................................................................
                                     ...................................................................................................
                                     ................................................................................................
                                     ...........................................................................
                                                                        ANGER MERUUL MODULES

                                                                                                                                       11



                                                                                                                                         
                                                            11
                                     2                                                                                                  
                                                                                                                                         
                                                      1
                                        
                                                                                                                                         
                                                                                                                                         
                                                                                                                                         
                                                                                                                                         
                                                      11
P : P := Q  P  P  P  P P P P P P  P  PPPP . Proof. Let
 :   P be the set of
all pair (, , , , ). The set of indecomposable representations
of  are in the set of posstive roots  ,            and              are

in this part of          .
Proof. Let   P  be the correspondence of    and    and     P  . The following proposit
ion is proved.
Proposition 3.1. The following proposition is
proved.
       (ii) There exists   , and    are all subsets of
 and  and  are a product of  and    and    and    and let
                                                                                                 
        
         =   Q                 Q                 . Th
en there
exists a unique   Q . Let    be a semisimple subset of    . Let  be the set of  -

tingular integers simple subspaces of    ,    and   Q . The set    and  and
                         ,  =            . We have  =   .
Remark. The category of all subgroups of the symmetric group S acts on the set of submanifold X and 
a completion
of trivial complex manifolds and the category of finite dimensional
representation theory of a closure of an irreducible representation of the symmetric groups are subg
roups and an admissible representation of the symmetric group S and
the corresponding algebra of the symplectic groups of type Q  
```


## Problems

The network seems to latch on to the spacing and formatting of the paper rather than the words. Often it will output a ton of periods and 1's ad nauseam. Occasionally one will find a paragraph of gibberish. I hypothesize that having the actual .tex files of the papers might allow for a better training dataset.

As for the pipeline, I would like to not have to use a bash script in the middle of the process, but current pdf to text python libraries destroy the content of the papers. 