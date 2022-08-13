---
tags:
- RequirementType
title: REQUIREMENT_PLOT_UNIT_TYPE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_UNIT_TYPE_MATCHES
>
> * Class: `PLOTS`
> * Arguments:
>	* UnitType `String`
>		* [Units.UnitType]
>	* LayerIndex `Integer`

## Samples

```SQL {title="PLOT_UNIT_IS_APOSTLE_REQUIREMENTS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"PLOT_UNIT_IS_APOSTLE_REQUIREMENTS",
		"REQUIREMENT_PLOT_UNIT_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"PLOT_UNIT_IS_APOSTLE_REQUIREMENTS",
		"LayerIndex",
		3
	),
	(
		"PLOT_UNIT_IS_APOSTLE_REQUIREMENTS",
		"UnitType",
		"UNIT_APOSTLE"
	);
	
```
