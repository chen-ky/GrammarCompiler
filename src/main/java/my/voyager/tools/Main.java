package my.voyager.tools;

import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

public class Main {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello world!");
        // create a CharStream that reads from standard input
        CharStream input = new ANTLRInputStream(System.in);

        // create a lexer that feeds off of input CharStream
        GrammarLangLexer lexer = new GrammarLangLexer(input);

        // create a buffer of tokens pulled from the lexer
        CommonTokenStream tokens = new CommonTokenStream(lexer);

        // create a parser that feeds off the tokens buffer
        GrammarLangParser parser = new GrammarLangParser(tokens);

        ParseTree tree = parser.init(); // begin parsing at init rule
//        System.out.println(tree.toStringTree());
        System.out.println(tree.toStringTree(parser)); // print LISP-style tree
    }
}