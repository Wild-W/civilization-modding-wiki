---
tags:
- RequirementType
title: REQUIREMENT_CITY_HAS_BUILDING
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_HAS_BUILDING
>
> * Class: `CITIES`
> * Arguments:
>	* MustBeFunctioning `Boolean`
>		* Require the building to be functioning (not pillaged).
>		* [Buildings.BuildingType]
>	* BuildingType `String`
>		* The type of the building to check for.
>		* [Buildings.BuildingType]

## Samples

```SQL {title="REQUIRES_NO_MARKET"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"REQUIRES_NO_MARKET",
		"REQUIREMENT_CITY_HAS_BUILDING",
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
		"REQUIRES_NO_MARKET",
		"BuildingType",
		"BUILDING_MARKET"
	),
	(
		"REQUIRES_NO_MARKET",
		"MustBeFunctioning",
		0
	);
	```

```SQL {title="REQUIRES_CITY_HAS_AMPHITHEATER"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_CITY_HAS_AMPHITHEATER",
		"REQUIREMENT_CITY_HAS_BUILDING"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_CITY_HAS_AMPHITHEATER",
		"BuildingType",
		"BUILDING_AMPHITHEATER"
	);
	```
