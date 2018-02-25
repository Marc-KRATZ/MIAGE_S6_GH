open Printf
open List

(******************************************************************************)
(*****  Reading functions  ****************************************************)
let read_line_int f =
  try
    let line = input_line f in
    let list_string = Str.split (Str.regexp "[ \t]+") line in
    map (int_of_string) list_string
  with
  | End_of_file -> begin
    print_string "File finished before it could read a line of int at position ";
    print_int (pos_in f);
    print_endline "";
    close_in f;
    exit 0;
    end
  | Failure "int_of_string" -> begin
    print_string "At position ";
    print_int (pos_in f);
    print_endline ", there should have been an int.";
    close_in f;
    exit 0;
    end
  | _ -> begin
    close_in f;
    print_endline "Unexpected behaviour in the read_line_int function";
    exit 0;
    end;;

let check_precision p s =
  if (String.contains s '.') then 
    let sint = Str.string_before s (String.index s '.') in
    let sfra = Str.string_after s ((String.index s '.')+1) in
    if ((String.length sfra) = p) then sint ^ sfra
    else failwith "wrong_fractional_part"
  else failwith "no_fractional_part";;
	
	(* p = precision *)
let read_line_float f p =
  try
    let line = input_line f in
    let list_string = Str.split (Str.regexp "[ \t]+") line in
    let list_prefloat = map (String.map (function c -> if (c = ',') then '.' else c)) list_string in
    let list_preint = map (check_precision p) list_prefloat in
    map (int_of_string) list_preint;
  with
  | End_of_file -> begin
    print_string "File finished before it could read a line of int at position ";
    print_int (pos_in f);
    print_endline "";
    close_in f;
    exit 0;
    end
  | Failure "int_of_string" -> begin
    print_string "At position ";
    print_int (pos_in f);
    print_endline ", there should have been an int.";
    close_in f;
    exit 0;
    end
  | Failure "wrong_fractional_part" -> begin
    print_string "At position ";
    print_int (pos_in f);
    print_endline ", the float written doesn't have the exact mandatory precision.";
    close_in f;
    exit 0;
    end
  | Failure "no_fractional_part" -> begin
    print_string "At position ";
    print_int (pos_in f);
    print_endline ", the float written doesn't have any fractional part.";
    close_in f;
    exit 0;
    end
  | _ -> begin
    close_in f;
    print_endline "Unexpected behaviour in the read_line_float function";
    exit 0;
    end;;

let rec read_lines f p =
  try
    let line = input_line f in
    let list_string = Str.split (Str.regexp "[ \t]+") line in
    let list_prefloat = map (String.map (function c -> if (c = ',') then '.' else c)) list_string in
    let list_preint = map (check_precision p) list_prefloat in
    (map (int_of_string) list_preint) :: (read_lines f p);
  with
  | End_of_file -> []
  | Failure "int_of_string" -> begin
    print_string "At position ";
    print_int (pos_in f);
    print_endline ", there should have been an int.";
    close_in f;
    exit 0;
    end
  | Failure "wrong_fractional_part" -> begin
    print_string "At position ";
    print_int (pos_in f);
    print_endline ", the float written doesn't have the exact mandatory precision.";
    close_in f;
    exit 0;
    end
  | Failure "no_fractional_part" -> begin
    print_string "At position ";
    print_int (pos_in f);
    print_endline ", the float written doesn't have any fractional part.";
    close_in f;
    exit 0;
    end
  | _ -> begin
    close_in f;
    print_endline "Unexpected behaviour in the read_line_float function";
    exit 0;
    end;;

let find_stock l b =
  let rec aux l1 n =
    match l1 with
    | [] -> 
      if ((n = 0) || (n != (n / b) * b)) then 
      begin
        print_string "Wrong number of evolution of prices or no profit.";
        exit 0;
      end
      else n / b
    | a :: lf -> aux lf (n+1) in
  match l with
  | [] -> begin
      print_endline "No evolution of prices nor profit.";
      exit 0;
    end
  | a :: lf -> aux lf 0;;
    




(******************************************************************************)
(*****  Arguments  *****)
let nbArg = Array.length Sys.argv;;
let fileName = ref "output";;
let check = ref 0;;

(*****  Help  *****)
if ((nbArg >= 2) && ((Sys.argv.(1) = "-h") || (Sys.argv.(1) = "-help") ||
  (Sys.argv.(1) = "--help")))
then begin
  print_endline 
"Usage: ./testAuto [fileName] [nbBieres stockBieres nbRepetition]\n";
  print_endline "Four typical usages exists :\n";
  print_endline "  ./testAuto";
  print_endline 
"      tests the output file named \"output\" and infers the arguments used\n";
  print_endline "  ./testAuto \"fileName\"";
  print_endline
"      tests the output file named \"fileName\" and infers the arguments used\n";
  print_endline "  ./testAuto b s n";
  print_endline
"      tests the output file named \"output\" under the assumption it was";
  print_endline
"        generated with the arguments :";
  print_endline
"          b : number of type of beers (positive int)";
  print_endline
"          s : stock of a type of beer (positive int)";
  print_endline
"          n : number of repetitions of the first buy simulation (positive int)\n";
  print_endline "  ./testAuto \"fileName\" b s n";
  print_endline
"      tests the output file named \"fileName\" under the assumption it was";
  print_endline
"        generated with the arguments :";
  print_endline
"          b : number of type of beers (positive int)";
  print_endline
"          s : stock of a type of beer (positive int)";
  print_endline
"          n : number of repetitions of the first buy simulation (positive int)\n";
  print_endline 
"Access to this help with the (only) argument : -h, -help or --help";
  exit 0;
end;;

(*****  Other arguments  *****)
if (nbArg = 2)
then fileName := Sys.argv.(1) else
if (nbArg = 4)
then check := 1 else
if (nbArg = 5)
then begin
  fileName := Sys.argv.(1);
  check := 2;
end else
if (nbArg != 1) 
then begin
  print_endline "You should check your arguments. Maybe ./testAuto -h could help";
  exit 0;
end;;

let check_arg i =
  try
    if (int_of_string Sys.argv.(i) <= 0)
    then begin
      print_endline "You should check your arguments (number of beers).";
      print_endline "Maybe ./testAuto -h could help";
      exit 0;
    end ;
    if (int_of_string Sys.argv.(i+1) <= 0)
    then begin
      print_endline "You should check your arguments (stock of a type of beer).";
      print_endline "Maybe ./testAuto -h could help";
      exit 0;
    end ;
    if (int_of_string Sys.argv.(i+2) <= 0)
    then begin
      print_endline "You should check your arguments (number of repetitions).";
      print_endline "Maybe ./testAuto -h could help";
      exit 0;
    end ;
  with
  | Failure "int_of_string" -> begin
      print_endline "You should check your arguments (string instead of int).";
      print_endline "Maybe ./testAuto -h could help";
      exit 0;
      end;
  | _ -> begin
      print_endline "You should check your arguments. Maybe ./testAuto -h could help";
      exit 0;
      end;;

if (!check != 0) then check_arg !check;;




(******************************************************************************)
(*****  Assist functions  *****)
let sum l =
  let rec aux l n =
    match l with
    | [] -> n
    | a :: lf -> aux lf (n + a) in
  aux l 0;;

let check_prices l b =
  let rec aux l =
    match l with
    |[] -> true 
    |a :: lf -> ((a / 5) * 5 = a) && (aux lf) in
  (length l = b) && (aux l);;
  
let check_evol l b s=
  let rec aux l n b=
    match (l,n) with
	|([],0) -> print_endline "fail : no profit line ?"
	|([a],0) -> 
	  if (length a = 1) 
	  then print_endline "ok"
	  else print_endline "fail : profit line doesn't contain a single number"
	|(a :: lf,0) -> print_endline "fail : too many lines"
	|(a :: lf,1) -> 
          let iter_and boo x = boo && (x = 0) in
	  if ((length a = b) && (fold_left iter_and true a))
	  then aux lf 0 b
	  else print_endline "fail : last line of evolution of prices doesn't have the right size"
	|([],n) -> print_endline "fail : not enough lines"
	|(a :: lf,n) -> 
	  if (length a = b) 
	  then aux lf (n-1) b
	  else print_endline "fail : one of your lines doesn't have the right size" in
  aux l (b * s) b


(******************************************************************************)
(*****  Read file  ******)
let ic = 
  try
    open_in !fileName
  with
  | _ -> begin
    print_string "testAuto failed to open file named \"";
    print_string !fileName;
    print_endline "\".";
    exit 0;
    end;;

let initPrices = read_line_float ic 2;;
let nbBeers = length initPrices;;
let initProba = read_line_float ic 3;;
let resultRepet = read_line_int ic;;
let nbRepet = sum resultRepet;;
let tmp = read_lines ic 2;;
close_in ic;;

let stock = find_stock tmp nbBeers;;

(*****  Check parameters  *****)
if (!check != 0) then begin
  print_endline "Checking if the manual parameters match those infered in the file :";
  if (nbBeers != int_of_string Sys.argv.(!check)) then begin
    print_endline "Number of beers : fail";
    print_endline "The number of beers in the file doesn't match your manual parameter.";
    print_endline "Proceeding with the rest and the infered value";
  end
  else print_endline "Number of beers : ok";
  if (stock != int_of_string Sys.argv.(!check + 1)) then begin
    print_endline "Stock of a type of beer : fail";
    print_endline "The stock number in the file doesn't match your manual parameter.";
    print_endline "Proceeding with the rest and the infered value";
  end
  else print_endline "Stock of a type of beer : ok";
  if (nbRepet != int_of_string Sys.argv.(!check +2)) then begin
    print_endline "Number of repetitions : fail";
    print_endline "The number of repetitions in the file doesn't match your manual parameter.";
    print_endline "Proceeding with the rest and the infered value";
  end
  else print_endline "Number of repetitions : ok";
end ;;

print_endline "\nUsing parameters :";
print_string "Number of beers : ";
print_int nbBeers;;
print_string "\nBeer stock : ";
print_int stock;;
print_string "\nNumber of repetitions : ";
print_int nbRepet;;
print_endline "\n";;

(*****  Check number of outputs  *****)
print_string "Checking first line : ";
if (check_prices initPrices nbBeers)
then print_endline "ok"
else print_endline "fail";;
print_string "Checking probabilities : ";
if (length initProba = nbBeers)
then print_endline "ok"
else print_endline "fail";;
print_string "Checking first buy simulations : ";
if (length resultRepet = nbBeers)
then print_endline "ok"
else print_endline "fail";;
print_string "Checking other lines : ";
check_evol tmp nbBeers stock;;

(*****  Check finished  *****)
print_endline "End of report.";;






