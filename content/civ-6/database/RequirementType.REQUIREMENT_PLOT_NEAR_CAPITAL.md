---
tags:
- RequirementType
title: REQUIREMENT_PLOT_NEAR_CAPITAL
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_NEAR_CAPITAL
>
> * Class: `PLOTS`
> * Arguments:
>	* MinDistance `Integer`
>	* MaxDistance `Integer`

## Samples

```SQL {title="REQUIRES_OBJECT_10_OR_MORE_TILES_FROM_CAPITAL"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_OBJECT_10_OR_MORE_TILES_FROM_CAPITAL",
		"REQUIREMENT_PLOT_NEAR_CAPITAL"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_OBJECT_10_OR_MORE_TILES_FROM_CAPITAL",
		"MinDistance",
		10
	);
	
```

```SQL {title="REQUIRES_OBJECT_6_TILES_FROM_CAPITAL"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_OBJECT_6_TILES_FROM_CAPITAL",
		"REQUIREMENT_PLOT_NEAR_CAPITAL"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_OBJECT_6_TILES_FROM_CAPITAL",
		"MaxDistance",
		6
	);
	
```
