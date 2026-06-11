function findDuplicatesIn(myArray) {
	let seen = [];
	let duplicates = [];

	for(let index = 0; index < myArray.length; index++) {
		let alreadyExist = false;
	}

	    for(let items : seen) {
		    if(items === index) {
			    alreadyExist = true;
			    break;
		    }
	    }

	if(alreadyExist) {
		alreadyDuplicate = false;
	}

	    for(let duplicateItems : duplicates) {
		    if(duplicateItems === index) {
			    alreadyDuplicate = true;
			    break;
		    }
	    }
	    if(!alreadyDuplicate) {
		    duplicates.push(index[myArray])
	    }

}
