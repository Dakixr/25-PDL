
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightALERTINPUTIFELSERETURNrightFUNCTIONrightBOOLEANSTRINGNUMBERrightLETrightASSIGNREMAINDERleftNEGATIONleftGREATERTLESSTleftPLUSMINUSrightIDCONSTNUMCHAINleftLBRACKETRBRACKETleftLPARENTRPARENTALERT ASSIGN BOOLEAN CHAIN COMMA CONSTNUM ELSE FUNCTION GREATERT ID IF INPUT LBRACKET LESST LET LPARENT MINUS NEGATION NUMBER PLUS RBRACKET REMAINDER RETURN RPARENT SEMICOLON STRINGAxioma_ : AxiomaAxioma : Sentencia AxiomaAxioma : Funcion AxiomaAxioma : emptySentencia : SSentencia : IF_Sentencia : LET Tipo ID SEMICOLONIF_ : IF1 IF2IF1 : IF LPARENT E RPARENT SentenIF2 : ELSE SentenIF2 : emptySenten : SentenciaSenten : LBRACKET Lista_Sentencias RBRACKETS : ID ASSIGN E SEMICOLONS : ID REMAINDER E SEMICOLONS : ID LPARENT Parametros RPARENT SEMICOLONS : ALERT LPARENT E RPARENT SEMICOLONS : INPUT LPARENT ID RPARENT SEMICOLONS : RETURN X SEMICOLONParametros : E K2Parametros : emptyK2 : COMMA E K2K2 : emptyX : EX : emptyFuncion : F1 F2 F3F1 : FUNCTION Tipo_B IDF2 : LPARENT Cabecera RPARENTF3 : LBRACKET Lista_Sentencias RBRACKETTipo : BOOLEANTipo : NUMBERTipo : STRINGTipo_B : TipoTipo_B : emptyCabecera : Tipo ID KCabecera : emptyK : COMMA Tipo ID KK : emptyLista_Sentencias : Sentencia Lista_SentenciasLista_Sentencias : emptyE : NEGATION VE : RR : R GREATERT UR : R LESST UR : UU : U PLUS VU : U MINUS VU : VV : IDV : LPARENT E RPARENTV : ID LPARENT Parametros RPARENTV : CONSTNUMV : CHAINempty :'
    
_lr_action_items = {'LET':([0,3,4,6,7,14,41,42,43,54,55,61,69,70,71,74,75,76,82,95,96,98,103,104,106,107,],[8,8,8,-5,-6,-54,-8,8,-11,-26,8,-19,-10,-12,8,-7,-14,-15,8,8,-16,-29,-17,-18,-13,-9,]),'$end':([0,1,2,3,4,5,6,7,14,17,18,41,43,54,61,69,70,74,75,76,96,98,103,104,106,107,],[-54,0,-1,-54,-54,-4,-5,-6,-54,-2,-3,-8,-11,-26,-19,-10,-12,-7,-14,-15,-16,-29,-17,-18,-13,-9,]),'ID':([0,3,4,6,7,13,14,15,19,20,21,22,23,24,25,28,29,33,38,41,42,43,44,45,46,47,54,55,57,61,63,64,65,66,67,69,70,71,74,75,76,79,82,95,96,98,103,104,106,107,109,],[9,9,9,-5,-6,37,-54,-54,48,-30,-31,-32,37,37,37,37,60,37,37,-8,9,-11,72,-33,-34,37,-26,9,85,-19,37,37,37,37,37,-10,-12,9,-7,-14,-15,37,9,9,-16,-29,-17,-18,-13,-9,110,]),'ALERT':([0,3,4,6,7,14,41,42,43,54,55,61,69,70,71,74,75,76,82,95,96,98,103,104,106,107,],[11,11,11,-5,-6,-54,-8,11,-11,-26,11,-19,-10,-12,11,-7,-14,-15,11,11,-16,-29,-17,-18,-13,-9,]),'INPUT':([0,3,4,6,7,14,41,42,43,54,55,61,69,70,71,74,75,76,82,95,96,98,103,104,106,107,],[12,12,12,-5,-6,-54,-8,12,-11,-26,12,-19,-10,-12,12,-7,-14,-15,12,12,-16,-29,-17,-18,-13,-9,]),'RETURN':([0,3,4,6,7,14,41,42,43,54,55,61,69,70,71,74,75,76,82,95,96,98,103,104,106,107,],[13,13,13,-5,-6,-54,-8,13,-11,-26,13,-19,-10,-12,13,-7,-14,-15,13,13,-16,-29,-17,-18,-13,-9,]),'FUNCTION':([0,3,4,6,7,14,41,43,54,61,69,70,74,75,76,96,98,103,104,106,107,],[15,15,15,-5,-6,-54,-8,-11,-26,-19,-10,-12,-7,-14,-15,-16,-29,-17,-18,-13,-9,]),'IF':([0,3,4,6,7,14,41,42,43,54,55,61,69,70,71,74,75,76,82,95,96,98,103,104,106,107,],[16,16,16,-5,-6,-54,-8,16,-11,-26,16,-19,-10,-12,16,-7,-14,-15,16,16,-16,-29,-17,-18,-13,-9,]),'RBRACKET':([6,7,14,41,43,55,61,69,70,71,74,75,76,81,82,83,94,96,99,103,104,106,107,],[-5,-6,-54,-8,-11,-54,-19,-10,-12,-54,-7,-14,-15,98,-54,-40,106,-16,-39,-17,-18,-13,-9,]),'ELSE':([6,7,14,41,43,61,69,70,74,75,76,96,103,104,106,107,],[-5,-6,42,-8,-11,-19,-10,-12,-7,-14,-15,-16,-17,-18,-13,-9,]),'BOOLEAN':([8,15,27,101,],[20,20,20,20,]),'NUMBER':([8,15,27,101,],[21,21,21,21,]),'STRING':([8,15,27,101,],[22,22,22,22,]),'ASSIGN':([9,],[23,]),'REMAINDER':([9,],[24,]),'LPARENT':([9,10,11,12,13,16,23,24,25,28,33,37,38,47,63,64,65,66,67,72,79,],[25,27,28,29,38,47,38,38,38,38,38,67,38,38,38,38,38,38,38,-27,38,]),'NEGATION':([13,23,24,25,28,38,47,67,79,],[33,33,33,33,33,33,33,33,33,]),'SEMICOLON':([13,30,31,32,34,35,36,37,39,40,48,49,50,62,77,86,87,88,89,90,91,93,105,],[-54,61,-24,-25,-48,-42,-45,-49,-52,-53,74,75,76,-41,96,103,104,-43,-44,-46,-47,-50,-51,]),'CONSTNUM':([13,23,24,25,28,33,38,47,63,64,65,66,67,79,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'CHAIN':([13,23,24,25,28,33,38,47,63,64,65,66,67,79,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'RPARENT':([25,27,34,35,36,37,39,40,51,52,53,56,58,59,60,62,67,68,73,78,80,85,88,89,90,91,92,93,97,100,102,105,108,110,111,],[-54,-54,-48,-42,-45,-49,-52,-53,77,-54,-21,84,-36,86,87,-41,-54,93,95,-20,-23,-54,-43,-44,-46,-47,105,-50,-54,-35,-38,-51,-22,-54,-37,]),'LBRACKET':([26,42,84,95,],[55,71,-28,71,]),'PLUS':([34,36,37,39,40,88,89,90,91,93,105,],[-48,65,-49,-52,-53,65,65,-46,-47,-50,-51,]),'MINUS':([34,36,37,39,40,88,89,90,91,93,105,],[-48,66,-49,-52,-53,66,66,-46,-47,-50,-51,]),'GREATERT':([34,35,36,37,39,40,88,89,90,91,93,105,],[-48,63,-45,-49,-52,-53,-43,-44,-46,-47,-50,-51,]),'LESST':([34,35,36,37,39,40,88,89,90,91,93,105,],[-48,64,-45,-49,-52,-53,-43,-44,-46,-47,-50,-51,]),'COMMA':([34,35,36,37,39,40,52,62,85,88,89,90,91,93,97,105,110,],[-48,-42,-45,-49,-52,-53,79,-41,101,-43,-44,-46,-47,-50,79,-51,101,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Axioma_':([0,],[1,]),'Axioma':([0,3,4,],[2,17,18,]),'Sentencia':([0,3,4,42,55,71,82,95,],[3,3,3,70,82,82,82,70,]),'Funcion':([0,3,4,],[4,4,4,]),'empty':([0,3,4,13,14,15,25,27,52,55,67,71,82,85,97,110,],[5,5,5,32,43,46,53,58,80,83,53,83,83,102,80,102,]),'S':([0,3,4,42,55,71,82,95,],[6,6,6,6,6,6,6,6,]),'IF_':([0,3,4,42,55,71,82,95,],[7,7,7,7,7,7,7,7,]),'F1':([0,3,4,],[10,10,10,]),'IF1':([0,3,4,42,55,71,82,95,],[14,14,14,14,14,14,14,14,]),'Tipo':([8,15,27,101,],[19,45,57,109,]),'F2':([10,],[26,]),'X':([13,],[30,]),'E':([13,23,24,25,28,38,47,67,79,],[31,49,50,52,59,68,73,52,97,]),'V':([13,23,24,25,28,33,38,47,63,64,65,66,67,79,],[34,34,34,34,34,62,34,34,34,34,90,91,34,34,]),'R':([13,23,24,25,28,38,47,67,79,],[35,35,35,35,35,35,35,35,35,]),'U':([13,23,24,25,28,38,47,63,64,67,79,],[36,36,36,36,36,36,36,88,89,36,36,]),'IF2':([14,],[41,]),'Tipo_B':([15,],[44,]),'Parametros':([25,67,],[51,92,]),'F3':([26,],[54,]),'Cabecera':([27,],[56,]),'Senten':([42,95,],[69,107,]),'K2':([52,97,],[78,108,]),'Lista_Sentencias':([55,71,82,],[81,94,99,]),'K':([85,110,],[100,111,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Axioma_","S'",1,None,None,None),
  ('Axioma_ -> Axioma','Axioma_',1,'p_Axioma_prima','analizador_sintactico.py',36),
  ('Axioma -> Sentencia Axioma','Axioma',2,'p_Axioma_sentencia','analizador_sintactico.py',44),
  ('Axioma -> Funcion Axioma','Axioma',2,'p_Axioma_funcion','analizador_sintactico.py',52),
  ('Axioma -> empty','Axioma',1,'p_Axioma_empty','analizador_sintactico.py',60),
  ('Sentencia -> S','Sentencia',1,'p_Sentencia_S','analizador_sintactico.py',65),
  ('Sentencia -> IF_','Sentencia',1,'p_Sentencia_IF','analizador_sintactico.py',70),
  ('Sentencia -> LET Tipo ID SEMICOLON','Sentencia',4,'p_Sentencia_tipo_id','analizador_sintactico.py',75),
  ('IF_ -> IF1 IF2','IF_',2,'p_IF_IF1_IF2','analizador_sintactico.py',82),
  ('IF1 -> IF LPARENT E RPARENT Senten','IF1',5,'p_IF1','analizador_sintactico.py',87),
  ('IF2 -> ELSE Senten','IF2',2,'p_IF2','analizador_sintactico.py',95),
  ('IF2 -> empty','IF2',1,'p_IF2_empty','analizador_sintactico.py',100),
  ('Senten -> Sentencia','Senten',1,'p_Senten','analizador_sintactico.py',105),
  ('Senten -> LBRACKET Lista_Sentencias RBRACKET','Senten',3,'p_Senten_Lista','analizador_sintactico.py',110),
  ('S -> ID ASSIGN E SEMICOLON','S',4,'p_S_Asignacion','analizador_sintactico.py',115),
  ('S -> ID REMAINDER E SEMICOLON','S',4,'p_S_Asignacion_Remainder','analizador_sintactico.py',128),
  ('S -> ID LPARENT Parametros RPARENT SEMICOLON','S',5,'p_S_Funcion','analizador_sintactico.py',136),
  ('S -> ALERT LPARENT E RPARENT SEMICOLON','S',5,'p_S_Alert','analizador_sintactico.py',159),
  ('S -> INPUT LPARENT ID RPARENT SEMICOLON','S',5,'p_S_Input','analizador_sintactico.py',167),
  ('S -> RETURN X SEMICOLON','S',3,'p_S_Return','analizador_sintactico.py',179),
  ('Parametros -> E K2','Parametros',2,'p_Parametros_E_K2','analizador_sintactico.py',187),
  ('Parametros -> empty','Parametros',1,'p_Parametros_lambda','analizador_sintactico.py',195),
  ('K2 -> COMMA E K2','K2',3,'p_K2_comma','analizador_sintactico.py',200),
  ('K2 -> empty','K2',1,'p_K2_lambda','analizador_sintactico.py',208),
  ('X -> E','X',1,'p_X','analizador_sintactico.py',213),
  ('X -> empty','X',1,'p_X_lambda','analizador_sintactico.py',218),
  ('Funcion -> F1 F2 F3','Funcion',3,'p_Funcion','analizador_sintactico.py',223),
  ('F1 -> FUNCTION Tipo_B ID','F1',3,'p_F1','analizador_sintactico.py',231),
  ('F2 -> LPARENT Cabecera RPARENT','F2',3,'p_F2','analizador_sintactico.py',238),
  ('F3 -> LBRACKET Lista_Sentencias RBRACKET','F3',3,'p_F3','analizador_sintactico.py',244),
  ('Tipo -> BOOLEAN','Tipo',1,'p_Tipo_boolean','analizador_sintactico.py',249),
  ('Tipo -> NUMBER','Tipo',1,'p_Tipo_number','analizador_sintactico.py',255),
  ('Tipo -> STRING','Tipo',1,'p_Tipo_string','analizador_sintactico.py',261),
  ('Tipo_B -> Tipo','Tipo_B',1,'p_Tipo_B_Tipo','analizador_sintactico.py',267),
  ('Tipo_B -> empty','Tipo_B',1,'p_Tipo_B_lambda','analizador_sintactico.py',272),
  ('Cabecera -> Tipo ID K','Cabecera',3,'p_Cabecera_Tipo','analizador_sintactico.py',278),
  ('Cabecera -> empty','Cabecera',1,'p_Cabecera','analizador_sintactico.py',294),
  ('K -> COMMA Tipo ID K','K',4,'p_K','analizador_sintactico.py',299),
  ('K -> empty','K',1,'p_K1','analizador_sintactico.py',307),
  ('Lista_Sentencias -> Sentencia Lista_Sentencias','Lista_Sentencias',2,'p_Lista_Sentencias','analizador_sintactico.py',312),
  ('Lista_Sentencias -> empty','Lista_Sentencias',1,'p_Lista_Sentencias1','analizador_sintactico.py',317),
  ('E -> NEGATION V','E',2,'p_E','analizador_sintactico.py',322),
  ('E -> R','E',1,'p_E1','analizador_sintactico.py',330),
  ('R -> R GREATERT U','R',3,'p_R','analizador_sintactico.py',335),
  ('R -> R LESST U','R',3,'p_R1','analizador_sintactico.py',344),
  ('R -> U','R',1,'p_R2','analizador_sintactico.py',352),
  ('U -> U PLUS V','U',3,'p_U','analizador_sintactico.py',357),
  ('U -> U MINUS V','U',3,'p_U1','analizador_sintactico.py',365),
  ('U -> V','U',1,'p_U_V','analizador_sintactico.py',373),
  ('V -> ID','V',1,'p_V','analizador_sintactico.py',378),
  ('V -> LPARENT E RPARENT','V',3,'p_V1','analizador_sintactico.py',383),
  ('V -> ID LPARENT Parametros RPARENT','V',4,'p_V2','analizador_sintactico.py',388),
  ('V -> CONSTNUM','V',1,'p_V3','analizador_sintactico.py',393),
  ('V -> CHAIN','V',1,'p_V4','analizador_sintactico.py',398),
  ('empty -> <empty>','empty',0,'p_empty','analizador_sintactico.py',404),
]
