---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_AT_LEAST_NUM_BUILDINGS
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_AT_LEAST_NUM_BUILDINGS
>
> * Class: `PLAYERS`
> * Arguments:
>	* BuildingType `String`
>		* [Buildings.BuildingType]
>	* Amount `Integer`

## Samples

```SQL {title="HAS_7_TEMPLES"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"HAS_7_TEMPLES",
		"REQUIREMENT_PLAYER_HAS_AT_LEAST_NUM_BUILDINGS"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"HAS_7_TEMPLES",
		"Amount",
		7
	),
	(
		"HAS_7_TEMPLES",
		"BuildingType",
		"BUILDING_TEMPLE_AMUN"
	);
	```
