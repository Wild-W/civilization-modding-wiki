---
tags:
- RequirementType
title: REQUIREMENT_CITY_HAS_X_TERRAIN_TYPE
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_HAS_X_TERRAIN_TYPE
>
> * Class: `CITIES`
> * Arguments:
>	* TerrainType `String`
>		* [Terrains.TerrainType]
>	* Hills `Boolean`
>	* Amount `Integer`

## Samples

```SQL {title="REQUIRES_CITY_HAS_5_SNOW"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_CITY_HAS_5_SNOW",
		"REQUIREMENT_CITY_HAS_X_TERRAIN_TYPE"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_CITY_HAS_5_SNOW",
		"Amount",
		5
	),
	(
		"REQUIRES_CITY_HAS_5_SNOW",
		"Hills",
		1
	),
	(
		"REQUIRES_CITY_HAS_5_SNOW",
		"TerrainType",
		"TERRAIN_SNOW"
	);
	
```
