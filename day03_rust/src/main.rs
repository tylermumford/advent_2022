use std::fs;

fn main() {
    println!("Hello, world!");
    let sample = get_input("sampleInput");
    let mut priority_sum = 0;

    for line in sample {
        println!("\t{line}");
        let doubled = find_doubled_item(&line);
        let priority = letter_to_priority(&doubled);
        println!("\t  {doubled} ({priority})");

        priority_sum += priority;
    }

    println!("priority sum: {priority_sum}");

    // Same as above, but with less output
    println!();

    let sample = get_input("input");
    let mut priority_sum = 0;

    for line in sample {
        let doubled = find_doubled_item(&line);
        let priority = letter_to_priority(&doubled);

        priority_sum += priority;
    }

    println!("priority sum: {priority_sum}")
}

fn get_input(filename: &str) -> Vec<String> {
    let contents = match fs::read_to_string(filename) {
        Ok(s) => s,
        Err(e) => panic!("cannot read {filename}: {e}")
    };

    let mut result = Vec::new();
    for line in contents.lines() {
        result.push(line.to_string())
    }
    result
}

fn find_doubled_item(rucksack: &String) -> char {
    let len = rucksack.len() / 2;
    let first = &rucksack[0..len];
    let second = &rucksack[len..];

    for f in first.chars() {
        for s in second.chars() {
            if s == f {
                return s
            }
        }
    }

    unimplemented!("not in problem bounds: {rucksack}")
}

fn letter_to_priority(letter: &char) -> u32 {
    match letter {
        'a'..='z' => (*letter as u32) - ('a' as u32) + 1,
        'A'..='Z' => (*letter as u32) - ('A' as u32) + 27,
        _ => unimplemented!("no priority for {letter}"),
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn super_basic() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }

    #[test]
    #[should_panic]
    fn get_input_panics() {
        get_input("");
    }

    #[test]
    fn get_input_works() {
        let input = get_input("sampleInput");

        assert_eq!(input.len(), 6);
    }

    #[test]
    fn find_doubled_item_works() {
        let result = find_doubled_item(&"abcdec".to_string());
        assert_eq!(result, 'c');
    }

    #[test]
    fn letter_to_priority_works() {
        let scores = Vec::from_iter(1..=52);
        let letters = help_letters();

        for i in 0..letters.len() {
            let s = letter_to_priority(&letters[i]);
            assert_eq!(scores[i], s);
        }
    }

    fn help_letters() -> Vec<char> {
        let mut v = Vec::new();
        let mut next = 'a' as u8;

        for incr in 0..=25 {
            let push = (next + incr) as char;
            v.push(push);
        }

        next = 'A' as u8;
        for incr in 0..=25 {
            let push = (next + incr) as char;
            v.push(push);
        }

        v
    }
}