---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_BUSHIDO
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_BUSHIDO
>
> * Class: `PLAYERS`
> * Parameters:
>	* StatementKey `String`

## Samples

```SQL {title="AGENDA_BUSHIDO"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_BUSHIDO",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_BUSHIDO",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_10_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_BUSHIDO",
		"StatementKey",
		"AGENDA_BUSHIDO_WARNING"
	);
	
```

