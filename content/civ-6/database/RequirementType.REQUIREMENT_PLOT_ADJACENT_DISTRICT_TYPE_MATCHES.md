---
tags:
- RequirementType
title: REQUIREMENT_PLOT_ADJACENT_DISTRICT_TYPE_MATCHES
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_ADJACENT_DISTRICT_TYPE_MATCHES
>
> * Class: `PLOTS`
> * Arguments:
>	* MustBeFunctioning `Boolean`
>	* MinRange `Integer`
>	* MaxRange `Integer`
>	* DistrictType `String`
>		* [Districts.DistrictType]

## Samples

```SQL {title="REQUIRES_PLOT_WITHIN_EIGHT_HOLY_SITE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLOT_WITHIN_EIGHT_HOLY_SITE",
		"REQUIREMENT_PLOT_ADJACENT_DISTRICT_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLOT_WITHIN_EIGHT_HOLY_SITE",
		"DistrictType",
		"DISTRICT_HOLY_SITE"
	),
	(
		"REQUIRES_PLOT_WITHIN_EIGHT_HOLY_SITE",
		"MaxRange",
		8
	),
	(
		"REQUIRES_PLOT_WITHIN_EIGHT_HOLY_SITE",
		"MinRange",
		0
	);
	```

```SQL {title="REQUIRES_PLOT_ADJACENT_HOLY_SITE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLOT_ADJACENT_HOLY_SITE",
		"REQUIREMENT_PLOT_ADJACENT_DISTRICT_TYPE_MATCHES"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLOT_ADJACENT_HOLY_SITE",
		"DistrictType",
		"DISTRICT_HOLY_SITE"
	),
	(
		"REQUIRES_PLOT_ADJACENT_HOLY_SITE",
		"MinRange",
		0
	);
	```

```SQL {title="REQUIRES_NOT_ADJACENT_TO_AQUEDUCT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"REQUIRES_NOT_ADJACENT_TO_AQUEDUCT",
		"REQUIREMENT_PLOT_ADJACENT_DISTRICT_TYPE_MATCHES",
		1
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_NOT_ADJACENT_TO_AQUEDUCT",
		"DistrictType",
		"DISTRICT_AQUEDUCT"
	),
	(
		"REQUIRES_NOT_ADJACENT_TO_AQUEDUCT",
		"MustBeFunctioning",
		0
	);
	```
