---
tags:
- RequirementType
title: REQUIREMENT_PLOT_ADJACENT_TO_OWNER
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_ADJACENT_TO_OWNER
>
> * Class: `PLOTS`
> * Arguments:
>	* MinDistance `Integer`
>	* MaxDistance `Integer`

## Samples

```SQL {title="10_PLOTS_AWAY_MAX_UNIT_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"10_PLOTS_AWAY_MAX_UNIT_REQUIREMENT",
		"REQUIREMENT_PLOT_ADJACENT_TO_OWNER"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"10_PLOTS_AWAY_MAX_UNIT_REQUIREMENT",
		"MaxDistance",
		10
	),
	(
		"10_PLOTS_AWAY_MAX_UNIT_REQUIREMENT",
		"MinDistance",
		0
	);
	
```

```SQL {title="ADJACENT_TO_OWNER"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"ADJACENT_TO_OWNER",
		"REQUIREMENT_PLOT_ADJACENT_TO_OWNER"
	);


```
