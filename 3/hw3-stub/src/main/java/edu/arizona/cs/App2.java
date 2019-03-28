package edu.arizona.cs;

import edu.stanford.nlp.simple.*;
import java.util.List;

/**
 * Just a dummy class to test a second maven profile
 *
 */
public class App2
{
    public static void main( String[] args )
    {
        System.out.println( "Hello other profile!!" );
        System.out.println("Command line arguments: ");
        for(int i = 0; i < args.length; i ++) {
        	System.out.println("Argument #" + i + ": " + args[i]);
        }

        Sentence sent = new Sentence("Lucy is in the sky with diamonds.");
        List<String> tokens = sent.words();
        List<String> lemmas = sent.lemmas();

        for(int i = 0; i < tokens.size(); i ++) {
        	System.out.println("Token #" + i + ": " + tokens.get(i));
        	System.out.println("Lemma #" + i + ": " + lemmas.get(i));
        }
    }
}
