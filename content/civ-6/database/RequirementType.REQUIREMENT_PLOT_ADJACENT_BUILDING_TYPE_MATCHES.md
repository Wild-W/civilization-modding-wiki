---
tags:
- RequirementType
title: REQUIREMENT_PLOT_ADJACENT_BUILDING_TYPE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_ADJACENT_BUILDING_TYPE_MATCHES
>
> * Class: `PLOTS`
> * Arguments:
>	* MinRange `Integer`
>	* MaxRange `Integer`
>	* BuildingType `String`
>		* [Buildings.BuildingType]

## Samples

```SQL {title="REQUIRES_PLOT_HAS_ARTEMIS_WITHIN_4"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLOT_HAS_ARTEMIS_WITHIN_4",
		"REQUIREMENT_PLOT_ADJACENT_BUILDING_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLOT_HAS_ARTEMIS_WITHIN_4",
		"BuildingType",
		"BUILDING_TEMPLE_ARTEMIS"
	),
	(
		"REQUIRES_PLOT_HAS_ARTEMIS_WITHIN_4",
		"MaxRange",
		4
	),
	(
		"REQUIRES_PLOT_HAS_ARTEMIS_WITHIN_4",
		"MinRange",
		0
	);
	```
