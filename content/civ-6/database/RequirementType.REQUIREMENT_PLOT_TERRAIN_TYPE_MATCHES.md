---
tags:
- RequirementType
title: REQUIREMENT_PLOT_TERRAIN_TYPE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_TERRAIN_TYPE_MATCHES
>
> * Class: `PLOTS`
> * Arguments:
>	* TerrainType `String`
>		* [Terrains.TerrainType]

## Samples

```SQL {title="PLOT_IS_DESERT_HILLS_TERRAIN_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"PLOT_IS_DESERT_HILLS_TERRAIN_REQUIREMENT",
		"REQUIREMENT_PLOT_TERRAIN_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"PLOT_IS_DESERT_HILLS_TERRAIN_REQUIREMENT",
		"TerrainType",
		"TERRAIN_DESERT_HILLS"
	);
	
```
