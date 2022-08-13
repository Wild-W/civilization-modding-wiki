---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_GOT_GREAT_PERSON
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_GOT_GREAT_PERSON
>
> * Class: `PLAYERS`
> * Arguments:
>	* MinimumDelta `Integer`
>	* GreatPersonRatio `Integer`

## Samples

```SQL {title="REQUIRES_LAGS_GREAT_PEOPLE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_LAGS_GREAT_PEOPLE",
		"REQUIREMENT_PLAYER_GOT_GREAT_PERSON"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_LAGS_GREAT_PEOPLE",
		"GreatPersonRatio",
		"-1.2"
	),
	(
		"REQUIRES_LAGS_GREAT_PEOPLE",
		"MinimumDelta",
		2
	);
	
```
