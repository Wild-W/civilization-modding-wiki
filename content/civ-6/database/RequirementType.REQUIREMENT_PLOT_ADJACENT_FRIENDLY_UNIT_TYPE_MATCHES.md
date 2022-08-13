---
tags:
- RequirementType
title: REQUIREMENT_PLOT_ADJACENT_FRIENDLY_UNIT_TYPE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_ADJACENT_FRIENDLY_UNIT_TYPE_MATCHES
>
> * Class: `PLOTS`
> * Arguments:
>	* UnitType `String`
>		* The unit type to match against
>		* [Units.UnitType]
>	* IncludeCenter `Boolean`
>		* Whether or not to include the center hex.

## Samples

```SQL {title="UNIT_ADJACENT_TO_GREAT_GENERAL"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"UNIT_ADJACENT_TO_GREAT_GENERAL",
		"REQUIREMENT_PLOT_ADJACENT_FRIENDLY_UNIT_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"UNIT_ADJACENT_TO_GREAT_GENERAL",
		"IncludeCenter",
		1
	),
	(
		"UNIT_ADJACENT_TO_GREAT_GENERAL",
		"UnitType",
		"UNIT_GREAT_GENERAL"
	);
	
```

```SQL {title="LLANERO_IS_ADJACENT_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"LLANERO_IS_ADJACENT_REQUIREMENT",
		"REQUIREMENT_PLOT_ADJACENT_FRIENDLY_UNIT_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"LLANERO_IS_ADJACENT_REQUIREMENT",
		"UnitType",
		"UNIT_COLOMBIAN_LLANERO"
	);
	
```
