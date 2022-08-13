---
tags:
- RequirementType
title: REQUIREMENT_PLOT_TERRAIN_CLASS_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_TERRAIN_CLASS_MATCHES
>
> * Class: `PLOTS`
> * Arguments:
>	* TerrainClass `String`
>		* The terrain class expected.
>		* [TerrainClasses.TerrainClassType]

## Samples

```SQL {title="PETRA_YIELD_MODIFIER_REQUIRES_PLOT_HAS_DESERT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"PETRA_YIELD_MODIFIER_REQUIRES_PLOT_HAS_DESERT",
		"REQUIREMENT_PLOT_TERRAIN_CLASS_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"PETRA_YIELD_MODIFIER_REQUIRES_PLOT_HAS_DESERT",
		"TerrainClass",
		"TERRAIN_CLASS_DESERT"
	);
	```
