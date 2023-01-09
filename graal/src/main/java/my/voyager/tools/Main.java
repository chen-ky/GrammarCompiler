// Reference: http://media.pragprog.com/titles/tpantlr2/code/tpantlr2-code.tgz
package my.voyager.tools;

import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

public class Main {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello world!");
        // create a CharStream that reads from standard input
        CharStream input = new ANTLRInputStream(System.in);

        // create a lexer that feeds off of input CharStream
        GLangLexer lexer = new GLangLexer(input);

        // create a buffer of tokens pulled from the lexer
        CommonTokenStream tokens = new CommonTokenStream(lexer);

        // create a parser that feeds off the tokens buffer
        GLangParser parser = new GLangParser(tokens);

        ParseTree tree = parser.init(); // begin parsing at init rule
//        System.out.println(tree.toStringTree());
        System.out.println(tree.toStringTree(parser)); // print LISP-style tree
    }
}