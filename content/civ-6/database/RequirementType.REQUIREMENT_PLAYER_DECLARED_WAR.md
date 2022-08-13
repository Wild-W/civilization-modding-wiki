---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_DECLARED_WAR
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_DECLARED_WAR
>
> * Class: `PLAYERS`
> * Arguments:
>	* WhileMet `Boolean`
>	* WarType `String`
>	* ExcludeEmergencies `Boolean`

## Samples

```SQL {title="REQUIRES_PLAYER_DECLARED_SURPRISE_WAR"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Triggered
	)
VALUES
	(
		"REQUIRES_PLAYER_DECLARED_SURPRISE_WAR",
		"REQUIREMENT_PLAYER_DECLARED_WAR",
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
		"REQUIRES_PLAYER_DECLARED_SURPRISE_WAR",
		"WarType",
		"SURPRISE_WAR"
	),
	(
		"REQUIRES_PLAYER_DECLARED_SURPRISE_WAR",
		"WhileMet",
		1
	);
	
```

```SQL {title="REQUIRES_PLAYER_DECLARED_JOINT_WAR"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_DECLARED_JOINT_WAR",
		"REQUIREMENT_PLAYER_DECLARED_WAR"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLAYER_DECLARED_JOINT_WAR",
		"WarType",
		"JOINT_WAR"
	);
	
```

```SQL {title="REQUIRES_PLAYER_DECLARED_WAR_EXCLUDE_SHARED_EMERGENCIES"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Triggered
	)
VALUES
	(
		"REQUIRES_PLAYER_DECLARED_WAR_EXCLUDE_SHARED_EMERGENCIES",
		"REQUIREMENT_PLAYER_DECLARED_WAR",
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
		"REQUIRES_PLAYER_DECLARED_WAR_EXCLUDE_SHARED_EMERGENCIES",
		"ExcludeEmergencies",
		1
	),
	(
		"REQUIRES_PLAYER_DECLARED_WAR_EXCLUDE_SHARED_EMERGENCIES",
		"WhileMet",
		1
	);
	
```

```SQL {title="REQUIRES_PLAYER_DECLARED_WAR"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Triggered
	)
VALUES
	(
		"REQUIRES_PLAYER_DECLARED_WAR",
		"REQUIREMENT_PLAYER_DECLARED_WAR",
		1
	);


```
