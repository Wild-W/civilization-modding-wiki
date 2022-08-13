---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_CITY_STATE_PROTECTOR
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_CITY_STATE_PROTECTOR
>
> * Class: `PLAYERS`
> * Arguments:
>	* UpperBound `Integer`
>	* NoUpperBound `Boolean`
>	* NoLowerBound `Boolean`
>	* LowerBound `Integer`

## Samples

```SQL {title="REQUIRES_HIGH_CITY_STATE_PROTECTION"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_HIGH_CITY_STATE_PROTECTION",
		"REQUIREMENT_PLAYER_CITY_STATE_PROTECTOR"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_HIGH_CITY_STATE_PROTECTION",
		"LowerBound",
		2
	),
	(
		"REQUIRES_HIGH_CITY_STATE_PROTECTION",
		"NoUpperBound",
		1
	);
	```

```SQL {title="REQUIRES_HIGH_CITY_STATE_AGGRESSION"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_HIGH_CITY_STATE_AGGRESSION",
		"REQUIREMENT_PLAYER_CITY_STATE_PROTECTOR"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_HIGH_CITY_STATE_AGGRESSION",
		"NoLowerBound",
		1
	),
	(
		"REQUIRES_HIGH_CITY_STATE_AGGRESSION",
		"UpperBound",
		"-2"
	);
	```
