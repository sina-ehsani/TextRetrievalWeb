import scala.io.Source
val filename = "docs.txt"
val it = Source.fromFile(filename).getLines().toList
// Normalize:
val normalize_docs = it.map(e => e.toLowerCase)
// Split: + Remove docs
val tokenize_docs = normalize_docs.map(e => e.split(" ").drop(1))

tokenize_docs(0).zipWithIndex.map{ case (s,i) => (s,1) }.toMap