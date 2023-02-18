use std::fs;

fn main() {
    println!("Hello, world!");
    let sample = get_input("sampleInput");
    for line in sample {
        println!("\t{line}")
    }
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
}