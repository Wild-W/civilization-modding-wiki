---
tags:
- RequirementType
title: REQUIREMENT_REQUIREMENTSET_IS_MET
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_REQUIREMENTSET_IS_MET
>
> * Class: `ANY`
> * Arguments:
>	* RequirementSetId `String`
>	* OnlyOwnersCity `Boolean`

## Samples

```SQL {title="AOE_REQUIRES_ATOMIC_REQUIREMENTS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"AOE_REQUIRES_ATOMIC_REQUIREMENTS",
		"REQUIREMENT_REQUIREMENTSET_IS_MET"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"AOE_REQUIRES_ATOMIC_REQUIREMENTS",
		"RequirementSetId",
		"AOE_ATOMIC_REQUIREMENTS"
	);
	
```

```SQL {title="REQUIRES_WARMONGER_TRIGGER"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_WARMONGER_TRIGGER",
		"REQUIREMENT_REQUIREMENTSET_IS_MET"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_WARMONGER_TRIGGER",
		"OnlyOwnersCity",
		0
	),
	(
		"REQUIRES_WARMONGER_TRIGGER",
		"RequirementSetId",
		"WARMONGER_TRIGGERS"
	);
	
```

```SQL {title="PLOT_IS_DESERT_OR_DESERT_HILLS_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"PLOT_IS_DESERT_OR_DESERT_HILLS_REQUIREMENT",
		"REQUIREMENT_REQUIREMENTSET_IS_MET"
	);


```
