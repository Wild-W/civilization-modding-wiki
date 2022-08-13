---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_GREAT_PERSON
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_GREAT_PERSON
>
> * Class: `PLAYERS`
> * Arguments:
>	* GreatPersonIndividual `String`

## Samples

```SQL {title="ALEXANDER_ELIMINATED"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"ALEXANDER_ELIMINATED",
		"REQUIREMENT_PLAYER_HAS_GREAT_PERSON",
		1
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"ALEXANDER_ELIMINATED",
		"GreatPersonIndividual",
		"GREAT_PERSON_INDIVIDUAL_ALEXANDER"
	);
	
```
