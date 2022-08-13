---
tags:
- RequirementType
title: REQUIREMENT_UNIT_PLOT_HAS_NATIONAL_PARK
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_UNIT_PLOT_HAS_NATIONAL_PARK
>
> * Class: `UNITS`
> * Arguments:
>	* SameOwner `Boolean`
>	* MinDistance `Integer`
>	* MaxDistance `Integer`

## Samples

```SQL {title="UNIT_OWNER_PARK_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"UNIT_OWNER_PARK_REQUIREMENT",
		"REQUIREMENT_UNIT_PLOT_HAS_NATIONAL_PARK"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"UNIT_OWNER_PARK_REQUIREMENT",
		"MaxDistance",
		2
	),
	(
		"UNIT_OWNER_PARK_REQUIREMENT",
		"MinDistance",
		0
	),
	(
		"UNIT_OWNER_PARK_REQUIREMENT",
		"SameOwner",
		1
	);
	
```
