// Adds an ingredient to your ingredient list
function addIngredient(e){
	var amountDiv = $(e).parent();
	var formGroup = amountDiv.parent();
	var allInputs = formGroup.find(":input");

	// Pass the inputs of the ingredients in to be checked for invalid numbers/selections
	if(validate(allInputs)){
		// Lots of manual stuff here.
		var amount = amountDiv.find("input").val(); // The actual number
		var amountMeasure = amountDiv.text().trim(); // oz/lbs
		var ingredientId = formGroup.find("select").val(); // IngredientId to build the next line
		var ingredientName = formGroup.find("option[value='" + ingredientId + "']").text(); // Ingredient name, American/Centenial/etc
		var ingredientType = formGroup.attr("data-ingredient-type"); // Ingredient Type, Yeast/Hops/etc

		// CommaSeparatedValue field to hold the ingredients
		var hiddenIngredientsText = $("#hiddenIngredients").val(); // Current text
		var addedIngredientText = ingredientId + ";"; // Text that needs to be added
		$("#hiddenIngredients").text(hiddenIngredientsText + addedIngredientText); // Adding it all together

		// See three lines above. Probably could write a small function that does this and consolodate this a little
		var hiddenAmountsText = $("#hiddenAmounts").val();
		var addedAmountText = amount + amountMeasure + ";";
		$("#hiddenAmounts").text(hiddenAmountsText + addedAmountText);

		// Builds the html for a list item and adds it to the summary and the ingredients screen
		var listItem = buildListItem(amount, amountMeasure, ingredientName, ingredientId);
		var summaryDestination = "#ingredientSummary" + ingredientType;
		addListItem(listItem, summaryDestination);

		// Same as above
		var addedIngredientsDestination = "#addedIngredients";
		addListItem(listItem, addedIngredientsDestination);

		// Resets the inputs
		formGroup.find("select").val(0);
		amountDiv.find("input").val("");
	}
}

// Combines the ingredient information into a <li> tag
function buildListItem(amount, amountMeasure, ingredientName, ingredientId){
	var listItem = "<li data-ingredient-id='" + ingredientId+"'>";
	listItem += amount + amountMeasure + " " + ingredientName;
	listItem += "</li>";

	return listItem;
}

// Appends html to an existing location
function addListItem(listItem, destination){
	$(destination).append(listItem);
}

// The submit button functionality 
function submitRecipe(e){
	// base url and all the necessary data
	var url = $.find("base")[0].href;
	var data = {
		csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
		ingredients: $("#hiddenIngredients").text(),
		amounts: $("#hiddenAmounts").text(),
		instructions: $("#beerInstructions").val(),
		title: $("#beerTitle").val(),
		description: $("#beerDescription").val()
	}
	$.ajax({
		url: url + "addrecipe/",
		type: "Post",
		data: data,
		success: function(result){
			// On success, alert that it was successful and reload the page
			alert("Beer successfully created!");
			window.location = $.find("base")[0].href;
		}
	});
}

// Adds a new ingredient to the database
function addNewIngredient(e){
	var modalContent = $(e).parent().parent();
	var ingredientTypeId = modalContent.find("select").val();
	var ingredientName = modalContent.find("input").val().trim();
	if(ingredientTypeId == 0 || ingredientName == ""){
		$("#ingredientAlert").show();
	}
	else{
		$("#ingredientAlert").hide();
		var url = $.find("base")[0].href;
		$.ajax({
			url: url + "addnewingredient/",
			type: "Post",
			data: {csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(), ingredient_type_id: ingredientTypeId, ingredient_name: ingredientName},
			success: function(result){
				// Parse the necessary info from the result
				var ingredientId = result.split(";")[0];
				var ingredientName = result.split(";")[1];
				var ingredientTypeName = result.split(";")[2];

				// Find the drop down that the ingredient belongs to
				var ingredientTypeDiv = $.find("div[data-ingredient-type='" + ingredientTypeName + "']");
				var ingredientTypeDropDown = $(ingredientTypeDiv).find("select");
				var ingredientOption = new Option(ingredientName, ingredientId);// "<select value='" + ingredientId + "'>" + ingredientName + "</select>";
				
				// Add ingredient to drop down and select it
				ingredientTypeDropDown.append(ingredientOption);
				ingredientTypeDropDown.val(ingredientId);
				$('#addIngredientModal').modal('toggle');
				
				// Reset the inputs on the modal
				var modalContent = $(e).parent().parent();
				modalContent.find("select").val(0);
				modalContent.find("input").val("");
				
			}
		});
	}
}



// Add info to summary page when clicked off.
$("#beerTitle").blur(function(){
	$("#summaryTitle").text(this.value);
});
$("#beerDescription").blur(function(){
	$("#summaryDescription").text(this.value);
});
$("#beerInstructions").blur(function(){
	$("#summaryInstructions").text(this.value);
});

// Validates inputs and checks for negative or null/empty values
function validate(inputs){
	var isValid = true;
	$.each(inputs, function(t, input){
		if(input.value <= 0 || input.value == ""){
			isValid = false;
			input.classList.add("alert");
		}
		else{
			input.classList.remove("alert");
		}
	});
	return isValid;
}