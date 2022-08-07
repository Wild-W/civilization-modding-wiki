---
tags:
- EffectType
title: EFFECT_ADD_PLAYER_PROJECT_AVAILABILITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADD_PLAYER_PROJECT_AVAILABILITY
>
> * Class: `Unknown`
> * Parameters:
>	* ProjectType `String`

## Samples
```SQL {title="AID_REQUEST_GRANT_PROJECT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"AID_REQUEST_GRANT_PROJECT",
		"MODIFIER_EMERGENCY_PLAYERS_MAKE_PROJECT_AVAILABLE",
		"EMERGENCY_MEMBER_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AID_REQUEST_GRANT_PROJECT",
		"ProjectType",
		"PROJECT_SEND_AID"
	);
	
```

