---
tags:
- RequirementType
title: REQUIREMENT_PLOT_NEARBY_UNIT_TAG_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_NEARBY_UNIT_TAG_MATCHES
>
> * Class: `PLOTS`
> * Arguments:
>	* Tag `String`
>	* MinDistance `Integer`
>	* MaxDistance `Integer`

## Samples

```SQL {title="TRADER_IS_WITHIN_FOUR_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"TRADER_IS_WITHIN_FOUR_REQUIREMENT",
		"REQUIREMENT_PLOT_NEARBY_UNIT_TAG_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"TRADER_IS_WITHIN_FOUR_REQUIREMENT",
		"MaxDistance",
		4
	),
	(
		"TRADER_IS_WITHIN_FOUR_REQUIREMENT",
		"MinDistance",
		0
	),
	(
		"TRADER_IS_WITHIN_FOUR_REQUIREMENT",
		"Tag",
		"CLASS_TRADER"
	);
	
```
