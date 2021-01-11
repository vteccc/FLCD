/* A Bison parser, made by GNU Bison 3.7.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2020 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    INT = 258,                     /* INT  */
    BOOL = 259,                    /* BOOL  */
    STRING = 260,                  /* STRING  */
    CHARACTER = 261,               /* CHARACTER  */
    IF = 262,                      /* IF  */
    ELSE = 263,                    /* ELSE  */
    WHILE = 264,                   /* WHILE  */
    FUNCTION = 265,                /* FUNCTION  */
    READ = 266,                    /* READ  */
    WRITE = 267,                   /* WRITE  */
    TRUE = 268,                    /* TRUE  */
    FALSE = 269,                   /* FALSE  */
    FOR = 270,                     /* FOR  */
    LENGTH = 271,                  /* LENGTH  */
    IDENTIFIER = 272,              /* IDENTIFIER  */
    CONSTANT = 273,                /* CONSTANT  */
    COLON = 274,                   /* COLON  */
    SEMI_COLON = 275,              /* SEMI_COLON  */
    COMA = 276,                    /* COMA  */
    DOT = 277,                     /* DOT  */
    PLUS = 278,                    /* PLUS  */
    MINUS = 279,                   /* MINUS  */
    MULTIPLY = 280,                /* MULTIPLY  */
    DIVISION = 281,                /* DIVISION  */
    FLOOR_DIVISION = 282,          /* FLOOR_DIVISION  */
    MODULO = 283,                  /* MODULO  */
    LEFT_ROUND_BRACKETS = 284,     /* LEFT_ROUND_BRACKETS  */
    RIGHT_ROUND_BRACKETS = 285,    /* RIGHT_ROUND_BRACKETS  */
    LEFT_SQUARE_BRACKETS = 286,    /* LEFT_SQUARE_BRACKETS  */
    RIGHT_SQUARE_BRACKETS = 287,   /* RIGHT_SQUARE_BRACKETS  */
    LEFT_CURLY_BRACKETS = 288,     /* LEFT_CURLY_BRACKETS  */
    RIGHT_CURLY_BRACKETS = 289,    /* RIGHT_CURLY_BRACKETS  */
    QUESTION_MARK = 290,           /* QUESTION_MARK  */
    LESS_THAN = 291,               /* LESS_THAN  */
    GREATER_THAN = 292,            /* GREATER_THAN  */
    LESS_OR_EQUAL_THAN = 293,      /* LESS_OR_EQUAL_THAN  */
    GREATER_OR_EQUAL_THAN = 294,   /* GREATER_OR_EQUAL_THAN  */
    DIFFERENT = 295,               /* DIFFERENT  */
    EQUAL = 296,                   /* EQUAL  */
    ASSIGNMENT = 297,              /* ASSIGNMENT  */
    AND_OPERATOR = 298,            /* AND_OPERATOR  */
    OR_OPERATOR = 299              /* OR_OPERATOR  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif
/* Token kinds.  */
#define YYEOF 0
#define YYerror 256
#define YYUNDEF 257
#define INT 258
#define BOOL 259
#define STRING 260
#define CHARACTER 261
#define IF 262
#define ELSE 263
#define WHILE 264
#define FUNCTION 265
#define READ 266
#define WRITE 267
#define TRUE 268
#define FALSE 269
#define FOR 270
#define LENGTH 271
#define IDENTIFIER 272
#define CONSTANT 273
#define COLON 274
#define SEMI_COLON 275
#define COMA 276
#define DOT 277
#define PLUS 278
#define MINUS 279
#define MULTIPLY 280
#define DIVISION 281
#define FLOOR_DIVISION 282
#define MODULO 283
#define LEFT_ROUND_BRACKETS 284
#define RIGHT_ROUND_BRACKETS 285
#define LEFT_SQUARE_BRACKETS 286
#define RIGHT_SQUARE_BRACKETS 287
#define LEFT_CURLY_BRACKETS 288
#define RIGHT_CURLY_BRACKETS 289
#define QUESTION_MARK 290
#define LESS_THAN 291
#define GREATER_THAN 292
#define LESS_OR_EQUAL_THAN 293
#define GREATER_OR_EQUAL_THAN 294
#define DIFFERENT 295
#define EQUAL 296
#define ASSIGNMENT 297
#define AND_OPERATOR 298
#define OR_OPERATOR 299

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
