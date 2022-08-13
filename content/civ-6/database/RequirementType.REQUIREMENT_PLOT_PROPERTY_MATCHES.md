---
tags:
- RequirementType
title: REQUIREMENT_PLOT_PROPERTY_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_PROPERTY_MATCHES
>
> * Class: `PLOTS`
> * Arguments:
>	* PropertyName `String`
>	* PropertyMinimum `String`

## Samples

```SQL {title="PLOT_IN_EDGELORD_ZONE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"PLOT_IN_EDGELORD_ZONE",
		"REQUIREMENT_PLOT_PROPERTY_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"PLOT_IN_EDGELORD_ZONE",
		"PropertyMinimum",
		1
	),
	(
		"PLOT_IN_EDGELORD_ZONE",
		"PropertyName",
		"EdgeLordZone"
	);
	```
