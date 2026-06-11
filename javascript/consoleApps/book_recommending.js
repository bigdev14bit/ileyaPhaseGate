const prompt = require("prompt-sync") ()

const books = [
      {"title": "Clean Code", "author": "Robert C. Martins", "genre": "Programming", "page": "462"},
      {"title": "Java How To Programmer", "author": "Paul Dietel", "genre": "Programming", "page": 1286},
      {"title": "A Woman Of Substance", "author": "Barbara Taylor Bradford", "genre": "Novel", "page": "2000"},
      {"title": "The Psychology of Persuasion", "author": "Robert B. Cialdini", "genre": "Socials", "page": "10000"},
      {"title": "Dune", "author": "Frank Herbert", "genre": "Sci-fi", "page": "8500"},
      {"title": "The alchemist", "author": "??", "genre": "Fiction", "page": "8000"},
      {"title": "The name of the wind", "author": "Patrick Rothfuss", "genre": "Fantasy", "page": "10000"}
        ]

function show_menu() {
    let menu = `
==============================================================================
WELCOME   TO   BOOK   RECOMMENDING   SYSTEM
==============================================================================

1. GET RECOMMENDATION.
2. ADD BOOK.
3. REMOVE BOOK.
4. UPDATE BOOK.
5. EXIT
==============================================================================
`
    return menu
}
console.log(show_menu())

function show_recommendation(books) {
    let recommended_book = Math.floor(Math.random() * books.length);

    console.log()
    console.log("=" * 50)
    console.log("----RECOMMENDING----")
    console.log()
    console.log(`TITLE------>   ${recommended_book["title"]}`)
    console.log(`AUTHOR----->   ${recommended_book["author"]}`)
    console.log(`GENRE------>   ${recommended_book["genre"]}`)
    console.log(`PAGE------->   ${recommended_book["page"]}`)
    console.log("=" * 50)
    console.log()
}

function add_book() {

    console.log()
    console.log("----ADD   BOOK----")

    let title = prompt("Title: ")
    let author = prompt("Author: ")
    let genre = prompt("Genre: ")
    let page = prompt("Page: ")

    let add_book = {
        "title": title,
        "author": author,
        "genre": genre,
        "page": page
            }

    books.push(add_book)

    console.log()
    console.log("----BOOK   ADDED   SUCCESSFULLY----")
    console.log()
    console.log("=" * 50)
    console.log(`TITLE------>   ${title}`)
    console.log(`AUTHOR----->   ${author}`)
    console.log(`GENRE------>   ${genre}`)
    console.log(`PAGE------->   ${page}`)
    console.log("=" * 50)
    console.log()
}

function remove_book() {
    console.log()
    console.log("----REMOVE   BOOK----")
    console.log()

    if(books.length == 0) {
        console.log()
        console.log("No Books To Remove In The System")
    }
    else {
        let counter = 1

        let remove_book = prompt("Did You Want To Remove Any Book: ")
        let clean_remove = remove_book.trim().toLowerCase()

        if(clean_remove != "no") {
            for(let book of books) {
                print(`${counter}: TITLE----->   ${book["title"]}`);
                counter = counter + 1;
	    }

            console.log();
            let number_of_book_to_remove = Number(prompt("Enter Number Of Book To Remove: "));
            if(number_of_book_to_remove <= 1 and number_of_book_to_remove >= books.length) {
                console.log("Errror, book not found!.");
	    }
            else {
                const book_to_remove = number_of_book_to_remove - 1;
                const deleted = books.pop(book_to_remove);

                console.log();
                console.log("=" * 50);
                console.log("Book Deleted Successfully");
                console.log(`REMOVED:----->   ${deleted["title"]}`);
                console.log("----Remaining",books.length,"Books.----");
                console.log("=" * 50);
                console.log();
	    }
	}
    }
}

function update_book() {

    console.log();
    console.log("----UPDATE   BOOK----");
    console.log();

    if(books.length == 0) {
        console.log();
        console.log("No Books To Update In The System");
    }
    else {
        counter = 1

        for(things of books) {
            console.log(`${counter}: TITLE----->   ${things["title"]}`)
            counter = counter + 1
        }

        console.log();
        let update_book = Number(prompt("Enter Number Of Book To Update: "));
        if(update_book <= 1 && update_book >= books.length) {
            console.log();
            console.log("Errror, book not found!.");
	}
        else {
            let book_to_update = update_book - 1;
            let selected_book = books[book_to_update];
	}
            menu = `
        YOU SELECETED:

TITLE:    "${selected_book["title"]}"
What Did You Want To Update??

1: Title.
2: Author's Name.
3: Genre Title.
4: Page Count.
                `

            console.log(menu);
            let update_input = Number(prompt("Enter Option: "));
            if(update_input == 1) {
                let title = prompt(`Change: ${selected_book["title"]} title: `);
                selected_book["title"] = title;
                console.log();
                console.log("Book Updated Successfully.");
                console.log(`New Title:  ${selected_book["title"]}`);
	    }

	    else if(update_input == 2) {
                let author = prompt(`Change: ${selected_book["author"]} author's name: `);
                selected_book["author"] = author;
                console.log();
                console.log("Book Updated Successfully.");
                console.log(`New Author's Name:  ${selected_book["author"]}`);
	    }

	    else if(update_input == 3) {
                let genre = prompt(`Change: ${selected_book["genre"]} genre title: `);
                selected_book["genre"] = genre;
                console.log();
                console.log("Book Updated Successfully.");
                console.log(`New Genre Title:  ${selected_book["genre"]}`);
	    }

	    else if(update_input == 4) {
                let page_count = Number(prompt(`Change: ${selected_book["page"]} page count: `))
                selected_book["page"] = page_count;
                console.log();
                console.log(f"Book Updated Successfully.");
                console.log(`New Page Count:  ${selected_book["page"]}`);
	    }

            else {
                console.log("Invalid Stuffs.");
	    }
}

while(true) {

    let userInput = prompt("Enter Option: ");
    if(userInput == "5") {
        console.log();
        console.log("Exit Successfully!!!");
        break;
    }

    else if(userInput == "1") {
        show_recommendation(books);
    }

    else if(userInput == "2") {
        add_book();
    }

    else if(userInput == "3") {
        remove_book();
    }

    else if(userInput == "4") {
        update_book();
    }

    else {
        console.log("Invalid Inputs.");
    }
}
