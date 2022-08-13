---
tags:
- RequirementType
title: REQUIREMENT_PLOT_ADJACENT_FRIENDLY_TERRITORY
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_ADJACENT_FRIENDLY_TERRITORY
>
> * Class: `PLOTS`
> * Arguments:
>	* MinRange `Integer`
>	* MaxRange `Integer`

## Samples

```SQL {title="IS_FRIENDLY_TERRITORY_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"IS_FRIENDLY_TERRITORY_REQUIREMENT",
		"REQUIREMENT_PLOT_ADJACENT_FRIENDLY_TERRITORY"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"IS_FRIENDLY_TERRITORY_REQUIREMENT",
		"MaxRange",
		0
	),
	(
		"IS_FRIENDLY_TERRITORY_REQUIREMENT",
		"MinRange",
		0
	);
	
```
