---
tags:
- RequirementType
title: REQUIREMENT_CITY_HAS_X_POPULATION
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_HAS_X_POPULATION
>
> * Class: `CITIES`
> * Arguments:
>	* Amount `Integer`

## Samples

```SQL {title="REQUIRES_CITY_HAS_7_POP"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_CITY_HAS_7_POP",
		"REQUIREMENT_CITY_HAS_X_POPULATION"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_CITY_HAS_7_POP",
		"Amount",
		7
	);
	```
